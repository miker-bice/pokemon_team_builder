from django.urls import path
from . import views

app_name = "pokemon"

urlpatterns = [
    path('', views.home, name='home'),
]