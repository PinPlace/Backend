from django.urls import path
from . import views

app_name ="pins"

urlpatterns = [
    path('', views.pins, name='pins'),
    path('create/', views.pin_create , name='create'),
    path('<slug:slug>/', views.pin_detail, name='pin_detail'),
]