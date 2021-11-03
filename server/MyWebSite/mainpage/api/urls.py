from django.urls import path
from mainpage.views import PageSettingsAPIView, PageContactsAPIView,PageContentAPIView

app_name="api_mainpage"


urlpatterns = [
   path("settings/", PageSettingsAPIView.as_view(), name="settings"),
   path("contacts/", PageContactsAPIView.as_view(), name="my_contacts"),
   # API for show contacts on mainpage api/contacts/
   path("page_content/", PageContentAPIView.as_view(), name="page_content"),
]