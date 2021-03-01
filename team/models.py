from django.db import models

# Create your models here.
class Teams(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    last_year_qualifiers = models.BooleanField(default=False)
