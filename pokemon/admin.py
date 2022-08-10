from django.contrib import admin
from .models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'team_name', 'description')

# Register your models here.
admin.site.register(Team, TeamAdmin)

