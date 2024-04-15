from rest_framework_simplejwt.authentication import JWTAuthentication
import logging

logger = logging.getLogger(__name__)

class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.jwt_authentication = JWTAuthentication()

    def __call__(self, request):
        # Attempt to authenticate the request
        try:
            auth_result = self.jwt_authentication.authenticate(request)
            print(auth_result)
            if auth_result is not None:
                user, token = auth_result
                request.user = user
                logger.debug(f"JWT Middleware: User authenticated with token: {token}")
            else:
                logger.debug("JWT Middleware: Authentication failed - no user/token found")
        except Exception as e:
            logger.error(f"JWT Middleware: Authentication failed: {e}")

        response = self.get_response(request)
        return response
