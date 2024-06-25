from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('home/', views.home, name='index'),
    # path('login/', views.login, name='login'),
    path('JuegosClasicos/', views.jclasicos, name='JuegosClasicos'),
    path('categorias/', views.categorias, name='categorias'),
    path('consolas/', views.consolas, name='consolas'),
    path('Indie/', views.indie, name='indie'),
    path('Administrar/', views.administrar, name='Administrar usuarios'),
    path('listado usuarios/', views.listauser, name='lista usuarios'),
    path('Registrate/<str:pk>', views.registro, name='registro'),
]