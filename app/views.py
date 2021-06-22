from django.shortcuts import render, redirect
from .models import Show

# Create your views here.

def index(request):
    return redirect('/shows')

def shows(request):
    context={
    'shows': Show.objects.all()
    }
    return render(request, 'index.html', context)

def show(request, id):
    context={
    'show': Show.objects.get(id=id)
    }

    return render(request, 'viewshow.html', context)

def new(request):

    return render(request, 'newshow.html')

def edit(request, id):
    context={
    'show': Show.objects.get(id=id)
    }
    return render(request, 'editshow.html', context)


def delete(request, id):
    pass