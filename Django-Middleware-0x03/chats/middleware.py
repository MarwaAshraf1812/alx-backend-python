from datetime import datetime
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
