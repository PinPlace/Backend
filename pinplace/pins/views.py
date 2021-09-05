from django.shortcuts import render
from django.http import HttpResponse
from .models import Pins

# def login(request):
#     return HttpResponse("<h1>Login page</h1>")

def pins(request):
    pins = Pins.objects.all().order_by('date_created')
    # context = { "pins": pins }
    return render(request, 'pins/pins.html', { 'pins': pins })

def pin_detail(request, slug):
    pin = Pins.objects.get(slug=slug)
    return render(request, 'pins/pin_detail.html', { 'pin':pin })