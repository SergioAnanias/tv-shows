from django.shortcuts import render, redirect, HttpResponse
from .models import Show
from django.contrib import messages
from django.http import JsonResponse

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
    if request.method == 'POST':
        print(request.POST)
        show_to_update= Show.objects.get(id=id)
        show_to_update.title= request.POST['title']
        show_to_update.network= request.POST['network']
        show_to_update.release= request.POST['release']
        show_to_update.desc= request.POST['desc']
        show_to_update.img= request.POST['img']
        show_to_update.save()
        messages.success(request, "Success")
    return redirect('/shows/' + str(show_to_update.id))

def create(request):
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect ('/shows/new')
    else:
        if request.method == 'POST':
            new_show = Show.objects.create(
                title=request.POST['title'], 
                network=request.POST['network'], 
                release=request.POST['release'],
                desc=request.POST['desc'],
                img=request.POST['img']
                )
            messages.success(request, "Success")
            return redirect('/shows/' + str(new_show.id))

def create_ajax(request):
    print(request.POST)
    errors = Show.objects.validator(request.POST)
    msgs = []
    if len(errors) > 0:
        for k, v in errors.items():
            msgs.append(v)
    if len(msgs) > 0:
        print(msgs)
        return JsonResponse({'msgs':msgs}, status=400)
    else:
        if request.method == 'POST':
            new_show = Show.objects.create(
                title=request.POST['title'], 
                network=request.POST['network'], 
                release=request.POST['release'],
                desc=request.POST['desc'],
                img=request.POST['img']
                )
            messages.success(request, "Success")
            return redirect('/shows/' + str(new_show.id))


def delete(request, id):
    delete = Show.objects.get(id=id)
    delete.delete()
    return redirect('/shows')