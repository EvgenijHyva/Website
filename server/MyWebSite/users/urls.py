from django.urls import path
from users.views import CurrentUserAPIView

app_name = "users_api"

urlpatterns = [
    path("user/", CurrentUserAPIView.as_view(), name="current_user"),
]