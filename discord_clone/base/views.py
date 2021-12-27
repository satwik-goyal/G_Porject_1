from io import TextIOWrapper
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Room, Topic
from .forms import RoomForm

# rooms = [
#     {'id': 1 , 'name': "python"},
#     {'id': 2 , 'name': "java"},
#     {'id': 3 , 'name': "c++"},

# ]

def login_p(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request , "user dosen't exists")

        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request , "uername or password is incorrect")

    return render(request , 'base/loginp.html')



def logoutuser(request):
    logout(request)
    return redirect('home')











def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__contains = q)|
        Q(name__contains = q) |
        Q(Discription__contains = q)
    )
    room_count = rooms.count()
    topics = Topic.objects.all()
    context = {"rooms": rooms, "topics" : topics , "room_count": room_count}
    return render(request , 'base/index.html' ,context )


@login_required(login_url = 'login')
def room(request , pk):
    room = Room.objects.get(id = pk)
    context = {"room" : room}
    return render(request, 'base/room.html', context)

@login_required(login_url = 'login')
def createroom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'forms': form}
    return render(request , 'base/room_form.html', context)

@login_required(login_url = 'login')
def updateroom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.user != room.host:
        return HttpResponse("fuck u")
    if request.method == 'POST':
        form = RoomForm(request.POST, instance= room)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'forms': form}
    return render(request , 'base/room_form.html', context)





@login_required(login_url = 'login')
def delete(request , pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    context = {'obj': room}
    return render(request , 'base/delete.html' , context)