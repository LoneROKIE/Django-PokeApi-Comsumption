from django.shortcuts import render
from django.http import  Http404 
import requests # importamos el modulo que instalamos antes

def pokemon(request):
    # Obtener el valor ingresado en la barra de búsqueda
    query = request.GET.get('q')

    # Obtener todos los pokemon de la API
    response = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=100&offset=00')
    pokemon = response.json()

    # Si hay una consulta, filtrar los resultados
    if query:
        pokemon_list = [p for p in pokemon['results'] if query.lower() in p['name'].lower()]
    else:
        pokemon_list = pokemon['results']

    context = {'pokemon_list': pokemon_list, 'query': query}
    return render(request, 'pokemons.html', context)

def pokemon_detail(request, pokemon_name):
    #pull data from third party res api
    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + pokemon_name)
    
    pokemon = response.json()
    
    context = {'pokemon': pokemon}
    
    return render(request, 'pokemon_details.html', context)
    

