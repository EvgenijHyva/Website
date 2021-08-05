from django.urls import path
from mainpage.views import PageSettingsAPIView


app_name="api_mainpage"


urlpatterns = [
   path("settings/", PageSettingsAPIView.as_view(), name="settings"),
]