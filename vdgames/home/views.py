from django.shortcuts import render
from .models import Usuarios

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
    usuario=Usuarios.objects.all()
    context={
        'usuario' : usuario
    }
    return render(request, 'home/Administrar usuarios.html', context)

def listauser (request):
    if request.method != "POST":
        usuario=Usuarios.objects.all()
        context={'usuario' : usuario}
        return render(request, 'home/lista usuarios.html', context)
    else:
        id=request.POST["id"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        contasena=request.POST["contrasena"]

        obj=Usuarios.objects.create(
            id_user=id,
            nombre=nombre, 
            apellido_paterno=aPaterno,
            apellido_materno=aMaterno,
            genero=genero,
            telefono=telefono,
            correo=email,
            contasena=contasena,
        )
        obj.save()
        context={'mensaje':"Datos almacenados de manera correcta"}
        return render(request, 'home/lista usuarios.html',context)


def registro (request):
    context={}
    return render(request, 'home/registro.html', context)

