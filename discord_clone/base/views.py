from django.shortcuts import render



rooms = [
    {'id': 1 , 'name': "python"},
    {'id': 2 , 'name': "java"},
    {'id': 3 , 'name': "c++"},

]
def home(request):
    context = {"rooms": rooms}
    return render(request , 'base/index.html' ,context )
def room(request):
    return render(request, 'base/room.html')
