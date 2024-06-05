from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacto/', views.contacto, name='contacto'),
    path('JuegosClasicos/', views.jclasicos, name='JuegosClasicos'),
    path('categorias/', views.categorias, name='categorias'),
    path('consolas/', views.consolas, name='consolas'),
    path('proximamente/', views.proximamente, name='proximamente'),
]