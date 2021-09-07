from pins.models import Pins
from django.shortcuts import get_object_or_404, redirect, render
from .models import Lists
from django.contrib.auth.decorators import login_required
from . import forms

def lists(request):
    lists = Lists.objects.all().order_by('date_created')
    return render(request, 'lists/lists.html', { 'lists': lists })

@login_required(login_url="/users/login")
def list_detail(request, slug):
    # item = get_object_or_404(Pins, slug=slug)
    if request.method =="POST":
        form = forms.CreateListPin(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = request.user
            instance.pin_id = request.pin_id
            instance.save()
            return redirect('list_detail', slug=slug)
    else: 
        list = Lists.objects.get(slug=slug)
        return render(request, 'lists/list_detail.html', {'list': list })

@login_required(login_url="/users/login")
def list_create(request):
    if request.method =="POST":
        form = forms.CreateList(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.user_id = request.user
            instance.save()
            slug = instance.slug
            return redirect('lists:list_detail', slug=slug)
    else:
        form = forms.CreateList()
        return render(request, 'lists/list_create.html', { "form": form })
