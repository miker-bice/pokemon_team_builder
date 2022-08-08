import re
from django.shortcuts import render
import requests


# this is the default home page
def home(request):
    # url = "https://pokeapi.co/api/v2/pokemon/mewtwo" #this is for single pokemon API calls

    #this is for batch pokemon API calls
    batch_url = "https://pokeapi.co/api/v2/pokemon?limit=10" 
    res = requests.get(batch_url)

    if res.status_code != 200:
        print(res.text)
    else:
        # GET batch pokemon data to API
        data = res.json()

        # make json object to list
        list_urls = [i for i in data['results']]        #this contains the urls of each pokemon from batch GET
        final_data = []
        animated_gifs = []

        # iterate over each urls
        for url in list_urls:
            response = requests.get(url['url'])

            if response.status_code != 200:
                print(response.text)
            else:
                # GET specific data of a pokemon
                new_data = response.json()

                #this is to extract the animated GIFs
                animated_gif = new_data['sprites']['versions']['generation-v']['black-white']['animated']['front_default']              

                #append the pokemon data and GIFs to array
                final_data.append(new_data)    
                animated_gifs.append(animated_gif)      
       
        # pass data as context object
        context = {
            'pokedata': final_data,
            'gifdata': animated_gifs
        }
        return render(request, 'pokemon/home.html', context)


def load_pokedex(request):
    
