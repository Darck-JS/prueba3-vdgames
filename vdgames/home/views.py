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

def indie (request):
    context={}
    return render(request, 'home/indie.html', context)

def administrar (request):
    context={}
    return render(request, 'home/Administrar usuarios.html', context)

def crud (request):
    context={}
    return render(request, 'home/crud.html', context)

def registro (request):
    context={}
    return render(request, 'home/registro.html', context)

