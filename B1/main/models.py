from django.db import models

class Tip(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    

# Create your models here.
