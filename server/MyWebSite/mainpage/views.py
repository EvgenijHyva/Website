from django.shortcuts import render
from rest_framework.generics import get_object_or_404, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from mainpage.api.serializers import PageSettingsSerializer, ContactsSerializer, PageContentSerializer
from mainpage.models import PageSettings, Contacts, PageContent
from MyWebSite.site_permisions import IsAuthorOrReadOnly
from users.models import CustomUser


def index(request):
    context = {
        "title": "MainPage"
    }
    return render(request, "mainpage/index.html", context)

def not_found(request, exception):
    context = {
        "title": "404 page not found",
        "text": "Сударь страницы нет!" if request.user.is_authenticated else "искомой страницы нет :(",
    }
    return render(request, "404.html", context)


class PageSettingsAPIView(RetrieveUpdateAPIView):
    serializer_class = PageSettingsSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_object(self):
        """user settings is related field in custom user model"""
        #return PageSettings.objects.filter(user=self.request.user).first() # same logic
        return CustomUser.objects.filter(pk=self.request.user.id).first().user_settings


class PageContactsAPIView(RetrieveAPIView): # ReadOnlyModelViewSet
    """Show my contacts if user is authorized"""
    serializer_class = ContactsSerializer
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        return Contacts.objects.first()



class PageContentAPIView(RetrieveAPIView):
    serializer_class = PageContentSerializer
    permission_classes = [IsAuthorOrReadOnly, ]

    def get_object(self):
        return PageContent.objects.first()



