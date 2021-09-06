from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Pins
from django.contrib.auth.decorators import login_required
from . import forms

def pins(request):
    pins = Pins.objects.all().order_by('date_created')
    return render(request, 'pins/pins.html', { 'pins': pins })

def pin_detail(request, slug):
    pin = Pins.objects.get(slug=slug)
    return render(request, 'pins/pin_detail.html', { 'pin': pin })

@login_required(login_url="/users/login/")
def pin_create(request):
    if request.method == "POST":
        form = forms.CreatePin(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('pins:pins')
    else:
        form = forms.CreatePin()
        return render(request, 'pins/pin_create.html', { "form": form })
