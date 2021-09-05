from django.urls import path
from . import views

app_name ="pins"

urlpatterns = [
    path('', views.pins, name='pins'),
    path('<slug:slug>/', views.pin_detail, name='pin_detail')
    # path('login/', views.login, name='login'),
]