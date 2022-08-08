from django.shortcuts import render
import requests

# Create your views here.

# this is the default home page
def home(request):
    # try doing a call to the API
    url = "https://pokeapi.co/api/v2/pokemon/mewtwo"
    res = requests.get(url)

    if res.status_code != 200:
        print(res.text)
    else:
        data = res.json()
        animated_gif = data['sprites']['versions']['generation-v']['black-white']['animated']['front_default']
        print(animated_gif)
        context = {
            'pokedata': data,
            'gifdata': animated_gif,
        }
        return render(request, 'pokemon/home.html', context)
