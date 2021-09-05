from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='users'),
    # path('login/', views.login, name='login'),
]