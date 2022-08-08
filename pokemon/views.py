from django.shortcuts import render

# Create your views here.

# this is the default home page
def home(request):
    return render(request, 'pokemon/home.html', {})
