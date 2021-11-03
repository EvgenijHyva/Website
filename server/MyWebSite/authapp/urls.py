from django.urls import path
from authapp.views import register, login, logout

app_name = "authapp"

urlpatterns = [
    path("old-login-form/", login, name="login"),
    path("old-register-form/", register, name="register"),
    path("logout/", logout, name="logout"),
]


