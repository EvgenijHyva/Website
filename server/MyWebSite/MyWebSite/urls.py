"""MyWebSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from mainpage.views import index
from core.views import IndexTemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("authapp.urls", namespace="auth")),
    path("api/", include("users.urls", namespace="api_users")),
    path("api/", include("mainpage.api.urls", namespace="api_mainpage")),
    path("forum/api/", include("forum.urls", namespace="api_forum")),
    path("api-auth/", include("rest_framework.urls")),  # аутентификация в api
    path("api/rest-auth/", include("rest_auth.urls")),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),  # registration in application
    path("accounts/", include("allauth.urls")),
    re_path("^.*$", IndexTemplateView.as_view(), name="entry_point"),
    #path("index/", index, name="entry_point")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

