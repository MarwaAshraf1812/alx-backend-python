from rest_framework_simplejwt.authentication import JWTAuthentication

def CustomJWTAuthentication(JWTAuthentication):
  def authenticate(self, request):
    result = super().authenticate(request)

    if result is None:
      return None
    
    user, token = result
    return user, token