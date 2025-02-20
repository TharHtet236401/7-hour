from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

rooms = [
    {'id': 1, 'name': 'Let\'s learn Python'},
    {'id': 2, 'name': 'Let\'s learn Django'},
    {'id': 3, 'name': 'Let\'s learn React'},
]

from .models import Room

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)