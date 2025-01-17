from django.http.response import HttpResponseForbidden
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    """
    A middleware that logs each user’s requests to a file,
    including the timestamp, user, and the request path.
    """

    def __init__(self, get_response):
        self.get_response = get_response

        self.logger = logging.getLogger(__name__) 
        handler = logging.FileHandler('requests.log')
        handler.setFormatter(logging.Formatter('%(message)s'))
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def __call__(self, request):
        # Log the request details before getting the response
        user = request.user if request.user.is_authenticated else 'Anonymous'
        log_message = f"{datetime.now()} - User: {user} - Path: {request.path}"
        self.logger.info(log_message)

        # Process the request and get the response
        response = self.get_response(request)
        return response

class RestrictAccessByTimeMiddleware:
    """
    A middleware that restricts access to
    the messaging up during certain hours of the day.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_time = datetime.now().time()
        restricted_hours = (21, 6)  # 6am to 8am
        # Check if the current time is within the restricted window
        if restricted_hours[0] <= current_time.hour or current_time.hour < restricted_hours[1]:
            return HttpResponseForbidden('Access restricted between 9 PM and 6 AM. Please try again later.')
        return self.get_response(request)  # If not restricted, proceed with the request
    

class OffensiveLanguageMiddleware:
    """
    A middleware that limits the number of chat messages a user
    can send within a certain time window, based on their IP address.
    """

    def __init__(self, get_response):
        self.get_response = get_response

        # Dictionary to store the message count for each IP address
        self.messages_count = {}
        self.messages_limit = 5  # Maximum messages allowed
        self.time_window = timedelta(minutes=1)  # Time window in seconds

    def __call__(self, request):
        if request.method == 'POST':
            ip_address = self.get_client_ip(request)
            current_time = datetime.now()

            if ip_address not in self.messages_count:
                self.messages_count[ip_address] = {'count': 0, 'timestamp': current_time}
            
            if current_time - self.messages_count[ip_address]['timestamp'] > self.time_window:
                self.messages_count[ip_address] = {'count': 0, 'timestamp': current_time}
            self.messages_count[ip_address]['count'] += 1
            
            if self.messages_count[ip_address]['count'] > self.messages_limit:
                logger.warning(f"Rate limit exceeded for IP: {ip_address}")
                return HttpResponseForbidden('Message limit exceeded. Please wait before sending more messages.')
        
        return self.get_response(request)
    

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
