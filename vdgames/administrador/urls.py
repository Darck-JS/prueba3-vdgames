from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('home/', views.home, name='home'),
    # path('administrador/', views.home, name='home'),
]