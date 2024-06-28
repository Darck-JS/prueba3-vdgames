from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# @login_required
# def menu (request):
#     context={}
#     return render(request, 'administrador/menu.html', context)

# def home (request):
#     context={}
#     return render(request, 'administrador/home.html', context)


@login_required
def menu(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        print("Es usuario")
        login(request, user)
        return render(request, 'administrador/menu.html', context)
    else:
        print("No es usuario")
    context = {}

def home(request):
    context = {}
    logout(request)
    return render(request, 'administrador/home.html', context)