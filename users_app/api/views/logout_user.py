from users_app.api.serializers.user_serializer import RegisterUserSerializer
from users_app.api.models import user_model
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.exceptions import TokenError# type: ignore
from rest_framework_simplejwt.tokens import RefreshToken# type: ignore
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.tokens import AccessToken

class LogoutUser(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # try:
        #     # Obtener el token asociado con el usuario
        #     token = Token.objects.get(user=request.user)
        #     # Eliminar el token
        #     token.delete()
        # except Token.DoesNotExist:
        #     return Response({"detail": "No token found for this user."}, status=status.HTTP_400_BAD_REQUEST)
        
        # return Response({"Log out success"},status=status.HTTP_200_OK)
        try:
            refresh_token = request.data.get('refresh_token')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
        except TokenError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"detail": "Logged out successfully."}, status=status.HTTP_200_OK)