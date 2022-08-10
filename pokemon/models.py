from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# pokemon team model
class Team(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    team_name = models.CharField(max_length=255, blank=False)
    description = models.TextField(max_length=255, blank=True)
    slot_1 = models.IntegerField(blank=False)
    slot_2 = models.IntegerField(blank=False)
    slot_3 = models.IntegerField(blank=False)
    slot_4 = models.IntegerField(blank=False)
    slot_5 = models.IntegerField(blank=False)
    slot_6 = models.IntegerField(blank=False, default=25)

    def __str__(self):
        return self.team_name
