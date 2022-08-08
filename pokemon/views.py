import re
from django.shortcuts import render
import requests

# Create your views here.

# this is the default home page
def home(request):
    # try doing a call to the API
    # url = "https://pokeapi.co/api/v2/pokemon/mewtwo" #this is for single pokemon API calls
    batch_url = "https://pokeapi.co/api/v2/pokemon?" #this is for batch pokemon API calls
    # res = requests.get(url)
    res = requests.get(batch_url)

    if res.status_code != 200:
        print(res.text)
    else:
        data = res.json()
        list_urls = [i for i in data['results']]
        final_data = []
        animated_gifs = []
        for url in list_urls:
            response = requests.get(url['url'])

            if response.status_code != 200:
                print(response.text)
            else:
                new_data = response.json()
                animated_gif = new_data['sprites']['versions']['generation-v']['black-white']['animated']['front_default']
                final_data.append(new_data)
                animated_gifs.append(animated_gif)

        # animated_gif = data['sprites']['versions']['generation-v']['black-white']['animated']['front_default']
       
        context = {
            'pokedata': final_data,
            'gifdata': animated_gifs,
        }
        return render(request, 'pokemon/home.html', context)
