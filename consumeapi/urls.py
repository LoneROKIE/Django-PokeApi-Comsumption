from django.urls import path # importamos path
from . import views # importamos las vistas

from django.urls import path
from . import views

urlpatterns = [
    path('', views.pokemon, name='pokemon'),
    path('<str:pokemon_name>/', views.pokemon_detail, name='pokemon_detail'),
]

