from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .forms import RoomForm
from .models import Room,Topic
from django.db.models import Q

rooms = [
    {'id': 1, 'name': 'Let\'s learn Python'},
    {'id': 2, 'name': 'Let\'s learn Django'},
    {'id': 3, 'name': 'Let\'s learn React'},
]

from .models import Room

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q))
    topics = Topic.objects.all()
    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'base/home.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def deleteRoom(request, pk):
    try:
        room = Room.objects.get(id=pk)
        if request.method == 'POST':
            room.delete()
            return redirect('home')
        
        context = {'obj': room}
        return render(request, 'base/delete.html', context)
    except Room.DoesNotExist:
        return HttpResponse("Room not found")
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")

