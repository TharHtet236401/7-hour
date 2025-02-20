from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

rooms = [
    {'id': 1, 'name': 'Room 1'},
    {'id': 2, 'name': 'Room 2'},
    {'id': 3, 'name': 'Room 3'},
]

def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request,pk):
    return render(request, 'base/room.html')