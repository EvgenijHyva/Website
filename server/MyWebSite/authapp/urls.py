from django.urls import path
from authapp.views import register, login, logout

app_name = "authapp"

urlpatterns = [
    path("login/", login, name="login"), #/auth/login/
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
]


