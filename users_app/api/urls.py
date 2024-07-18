from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path 
from users_app.api.views.registration_user import RegisterUser
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns =[
    path('login/',obtain_auth_token,name='login'),#genera token django
    path('register/',RegisterUser.as_view(),name='register'),#registrar usuario
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),#generar tokens con JWT
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]