from django.shortcuts import render 

# Create your views here.


def home (request):
    context={}
    return render(request, 'home/index.html', context)

def login (request):
    context={}
    return render(request, 'home/login.html', context)

def jclasicos (request):
    context={}
    return render(request, 'home/juegos clasicos.html', context)

def categorias (request):
    context={}
    return render(request, 'home/categorias.html', context)

def consolas (request):
    context={}
    return render(request, 'home/consolas.html', context)

def proximamente (request):
    context={}
    return render(request, 'home/proximamente.html', context)