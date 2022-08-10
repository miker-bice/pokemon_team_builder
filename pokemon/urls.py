from django.urls import path
from . import views

app_name = "pokemon"

urlpatterns = [
    path('', views.home, name='home'),
    path('load-pokedex/', views.load_pokedex, name='load-pokedex'),
    path('my-teams/', views.my_teams, name='my-teams'),
    path('create-team/', views.create_team, name='create-team'),
    path('generate-team/', views.generate_team, name='generate-team'),
    path('reshuffle/<int:data_id>', views.reshuffle, name='reshuffle'),
    path('save-team/', views.save_team, name='save-team'),
]
