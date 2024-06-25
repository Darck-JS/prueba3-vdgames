from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Colaboradores
from django.contrib.auth.decorators import login_required

from .forms import formuser

# Create your views here.

@login_required
def home (request):
    request.session["usuario"]
    usuario=request.session["usuario"]
    context={"usuario":usuario}
    return render(request, 'home/index.html', context)

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
    print("estoy en la funcion crud para el formulario")
    context={}

    if request.method == "POST":
        print("en el if post del crud para el formulario")
        form = formuser(request.POST)
        if form.is_valid:
            print("en el agregar, is_valid")
            form.save()

            # limpiar form
            form=formuser()

            context={'mensaje':"ok, datos grabados...","form":form}
            return render(request, 'home/Administrar usuarios.html', context)
        else:
            form=formuser()
            context={'form':form}
            return render(request, 'home/Administrar usuarios.html', context)

def listauser (request):
    if request.method != "POST":
        usuario=Colaboradores.objects.all()
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

        obj=Colaboradores.objects.create(
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

