from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('inicio/', views.index, name='index'),
    path('JuegosClasicos/', views.jclasicos, name='JuegosClasicos'),
    path('categorias/', views.categorias, name='categorias'),
    path('consolas/', views.consolas, name='consolas'),
    path('Indie/', views.indie, name='indie'),
    path('Administrar/', views.administrar, name='Administrar usuarios'),
    path('listado usuarios/', views.listauser, name='lista usuarios'),
    path('Registrate/', views.registro, name='registro'),
]