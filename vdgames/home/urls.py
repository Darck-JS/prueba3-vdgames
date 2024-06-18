from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('home/', views.home, name='index'),
    path('login/', views.login, name='login'),
    path('JuegosClasicos/', views.jclasicos, name='JuegosClasicos'),
    path('categorias/', views.categorias, name='categorias'),
    path('consolas/', views.consolas, name='consolas'),
    path('proximamente/', views.proximamente, name='proximamente'),
]