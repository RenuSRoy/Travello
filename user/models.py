from django.db import models

# Create your models here.

class Destinations(models.Model):
    image=models.FileField(upload_to="imgs")
    place=models.CharField(max_length=50)
    desc=models.CharField(max_length=400)
    price=models.CharField(max_length=50)
    



