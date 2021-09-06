from django.shortcuts import redirect, render
from django.http import HttpResponse
from rest_framework import mixins
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            #log user in
            return redirect('pins:pins')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', { 'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect('pins:pins')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', { 'form': form })

def logout_view(request):
    if request.method =='POST':
        logout(request)
        return redirect('users:login')

# class AuthViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin)