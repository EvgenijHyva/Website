from django.shortcuts import render
from rest_framework import viewsets, generics, status, mixins
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from mainpage.api.serializers import PageSettingsSerializer
from mainpage.models import PageSettings
from MyWebSite.site_permisions import IsAuthorOrReadOnly

class PageSettingsAPIView(generics.ListAPIView):
    serializer_class = PageSettingsSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        return PageSettings.objects.filter(user=self.request.user)
