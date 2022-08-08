from django.shortcuts import render
import requests

# Create your views here.

# this is the default home page
def home(request):
    # try doing a call to the API
    url = "https://pokeapi.co/api/v2/pokemon/pikachu"
    res = requests.get(url)

    if res.status_code != 200:
        print(res.text)
    else:
        data = res.json()
        context = {
            'pokedata':data
        }
        return render(request, 'pokemon/home.html', context)
