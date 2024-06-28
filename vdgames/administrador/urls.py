from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
]