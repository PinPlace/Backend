from django.urls import path
from .import views

app_name = "lists"

urlpatterns = [
    path('', views.lists, name='lists'),
    path('create/', views.list_create, name='create'),
    path('<slug:slug>/', views.list_detail, name='list_detail'),
]
