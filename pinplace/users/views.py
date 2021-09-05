from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import mixins

# Create your views here.

# def login(request):
#     return HttpResponse("<h1>Login page</h1>")

def users(request):
    return HttpResponse("<h1>reached the users page, meme</h1>")

# class AuthViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin)