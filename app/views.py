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

def editshow(request, id):
    print(request.POST)
    show_to_update= Show.objects.get(id=id)
    show_to_update.title= request.POST['title']
    show_to_update.network= request.POST['network']
    show_to_update.release= request.POST['release']
    show_to_update.desc= request.POST['desc']
    show_to_update.save()
    return redirect('/shows/' + str(show_to_update.id))

def create(request):
    new_show = Show.objects.create(
        title=request.POST['title'], 
        network=request.POST['network'], 
        release=request.POST['release'],
        desc=request.POST['desc']
        )
    return redirect('/shows/' + str(new_show.id))

def delete(request, id):
    delete = Show.objects.get(id=id)
    delete.delete()
    return redirect('shows/')