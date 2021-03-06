"""pinplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
from django.urls import path, include
# from users import views
from django.contrib.auth.models import User
from pins import views
from rest_framework import routers, serializers, viewsets, permissions

# Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


urlpatterns = [
    path('', include('pins.urls'))
    # path('admin/', admin.site.urls),
    # path('pins/', include('pins.urls')),
    # path('users/', include('users.urls')),
    # path('lists/', include('lists.urls')),
    # path('', views.pins, name='home'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('', include(router.urls)),
    # path("pinplace_logo.ico", RedirectView.as_view(url=staticfiles_storage.url("pinplace_logo.ico")))
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)