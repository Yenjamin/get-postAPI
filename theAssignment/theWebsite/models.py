from django.db import models

# Create your models here.

class pictureStore(models.Model):
    picture = models.ImageField()