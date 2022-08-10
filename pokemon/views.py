from django.shortcuts import render, redirect
from .randomize import randomize, single_randomize
from .models import Team
import requests


# this is the default home page
def home(request):
    return render(request, 'pokemon/home.html', {})


def load_pokedex(request):
    # request.session.flush()

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
       
        # pass data to sessions
        request.session['pokedata'] = {
            'pokemondata': final_data
        }

        request.session['animated'] = {
            'gif': animated_gifs
        }

        # context = {
        #     'pokedata': final_data,
        #     'gifdata': animated_gifs
        # }
        return redirect('pokemon:home')


def my_teams(request):
    # query the database here
    all_team_data = Team.objects.all().order_by('id')
    context = {
        'team_data': all_team_data
    }
    # get all the existing teams of a given user
    return render(request, 'pokemon/my_teams.html', context)


def create_team(request):
    
    return render(request, 'pokemon/create_team.html', {})


# this is for generating a line up for team 
def generate_team(request):
    # flush the sessions
    # request.session.flush()

    url = "https://pokeapi.co/api/v2/pokemon/"

    list_result = randomize(5)
    list_result.append(25)
    print("these are the results: ", str(list_result))
    team_data = []
    team_gifs = []

    # get the data of number from the PokeAPI   
    # iterate over each urls
    for number in list_result:
        response = requests.get(url + str(number))
        

        if response.status_code != 200:
            print(response.text)
        else:
            # GET specific data of a pokemon
            new_data = response.json()

            #this is to extract the animated GIFs
            animated_gif = new_data['sprites']['versions']['generation-v']['black-white']['animated']['front_default']              

            #append the pokemon data and GIFs to array
            team_data.append(new_data)    
            team_gifs.append(animated_gif)

    # print(team_data)             
    # pass data to sessions
    request.session['listresult'] = {
        'list_result': list_result
    }

    request.session['teamdata'] = {
        'lineup': team_data
    }

    request.session['teamgif'] = {
        'gif': team_gifs
    }


    return redirect('pokemon:create-team')



# for reshuffling a specific pokemon in team creation
def reshuffle(request, data_id):

    url = "https://pokeapi.co/api/v2/pokemon/"

    original = request.session['listresult']['list_result']
    # fetch the new team lineup
    new_lineup = single_randomize(original, data_id)

    team_data = []
    team_gifs = []

    # generate new data
    for number in new_lineup:
        response = requests.get(url + str(number))
    

        if response.status_code != 200:
            print(response.text)
        else:
            # GET specific data of a pokemon
            new_data = response.json()

            #this is to extract the animated GIFs
            animated_gif = new_data['sprites']['versions']['generation-v']['black-white']['animated']['front_default']              

            #append the pokemon data and GIFs to array
            team_data.append(new_data)    
            team_gifs.append(animated_gif)

    print(new_lineup)
    # save data to session
    request.session['listresult'] = {
        'list_result': new_lineup
    }

    request.session['teamdata'] = {
        'lineup': team_data
    }

    request.session['teamgif'] = {
        'gif': team_gifs
    }
    
    return redirect('pokemon:create-team')


# function for saving a generated team to database
def save_team(request):
    # simple validation
    if request.method == 'POST':
        # get data from the form
        team_name = request.POST['team_name']
        description = request.POST['team_desc']
        slot_0 = request.POST['slot_0']
        slot_1 = request.POST['slot_1']
        slot_2 = request.POST['slot_2']
        slot_3 = request.POST['slot_3']
        slot_4 = request.POST['slot_4']
        slot_5 = request.POST['slot_5']

        # create a new save item
        new_team = Team(
            team_name = team_name,
            description = description,
            slot_0 = slot_0,
            slot_1 = slot_1,
            slot_2 = slot_2,
            slot_3 = slot_3,
            slot_4 = slot_4,
            slot_5 = slot_5
        )

        # save to database
        new_team.save()

        # delete session keys
        del request.session['teamdata']
        del request.session['teamgif']

    else:
        return redirect('pokemon:create-team')

    return redirect('pokemon:my-teams')
