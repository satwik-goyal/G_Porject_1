from django.shortcuts import render
from .models import Room

rooms = [
    {'id': 1 , 'name': "python"},
    {'id': 2 , 'name': "java"},
    {'id': 3 , 'name': "c++"},

]
def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request , 'base/index.html' ,context )



def room(request , pk):
    room = Room.objects.get(id = pk)
    context = {"room" : room}
    return render(request, 'base/room.html', context)

def room_form(request):
    return render(request , 'base/room_form.html')
