from django.shortcuts import redirect, render
from .models import Lists
from django.contrib.auth.decorators import login_required
from . import forms

def lists(request):
    lists = Lists.objects.all().order_by('date_created')
    return render(request, 'lists/lists.html', { 'lists': lists })

def list_detail(request, slug):
    list = Lists.objects.get(slug=slug)
    return render(request, 'lists/list_detail.html', {'list': list })

@login_required(login_url="/users/login")
def list_create(request):
    if request.method =="POST":
        form = forms.CreateList(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('lists:lists')
    else:
        form = forms.CreateList()
        return render(request, 'lists/list_create.html', { "form": form })
