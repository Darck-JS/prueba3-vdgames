from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from home.models import Colaboradores,indie,registro_colaborador

# Create your views here.




@login_required
def menu(request):
    if request.method != "POST":
        usuario=Colaboradores.objects.all()
        context={'usuario' : usuario}
        return render(request, 'administrador/menu.html', context)
    else:
        id=request.POST["id"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]

        obj=Colaboradores.objects.create(
            id_user=id,
            nombre=nombre, 
            apellido_paterno=aPaterno,
            apellido_materno=aMaterno,
            genero=genero,
            telefono=telefono,
            correo=email,
        )
        obj.save()
        context={'mensaje':"Datos almacenados de manera correcta"}
    return render(request, 'administrador/menu.html', context)


def listado(request):
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