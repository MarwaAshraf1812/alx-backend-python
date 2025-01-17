from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
  def authenticate(self, request):
    result = super().authenticate(request)

    if result is None:
      return None
    
    user, token = result
    return user, token