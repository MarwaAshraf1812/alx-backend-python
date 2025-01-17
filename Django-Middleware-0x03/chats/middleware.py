from datetime import datetime
from django.http.response import HttpResponseForbidden
import logging

class RequestLoggingMiddleware:
    """
    A middleware that logs each user’s requests to a file,
    including the timestamp, user, and the request path.
    """

    def __init__(self, get_response):
        self.get_response = get_response

        # Set up logging
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
    implement a middleware that restricts access to
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
