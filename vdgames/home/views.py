from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Colaboradores
from django.contrib.auth.decorators import login_required
import requests
import json

from .forms import formuser


# Create your views here.

@login_required
def index (request):
    context={}
    return render(request, 'home/index.html', context)

@login_required
def jclasicos (request):
    context={}
    return render(request, 'home/juegos clasicos.html', context)

@login_required
def categorias(request):
    game_ids = ['grand-theft-auto-v', 'dota-2', 'team-fortress-2', 'counter-strike-global-offensive', 'unturned', 'rust', 'genshin-impact', 'valorant']  # Slugs de juegos de ejemplo
    api_key = '34ac3c3bfcf6460fbae69898fba58d69'
    api_url = 'https://api.rawg.io/api/games'
    games_data = []

    for game_id in game_ids:
        url = f'{api_url}/{game_id}?key={api_key}'

        try:
            response = requests.get(url)
            response.raise_for_status()
            game_data = response.json()

            if game_data:
                game_name = game_data.get('name')
                game_image_url = game_data.get('background_image')
                games_data.append({'id': game_id, 'name': game_name, 'image_url': game_image_url})

        except requests.exceptions.RequestException as e:
            print(f"Error al obtener los datos del juego con ID {game_id}: {e}")

    context = {
        'games': games_data
    }

    return render(request, 'home/categorias.html', context)


@login_required
def consolas (request):
    context={}
    return render(request, 'home/consolas.html', context)

@login_required
def indie (request):
    context={}
    return render(request, 'home/indie.html', context)

@login_required
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

@login_required
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

