from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
=======


def index(request):
    return render(request, 'index.html')


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })
>>>>>>> 06a30dab0c6fb0fdea09a6c572fecad485132f7c
