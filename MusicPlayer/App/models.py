from django.db import models
import datetime
from django.contrib.auth import get_user_model
from django.urls import reverse

class Artist(models.Model):
    artist_name = models.CharField(max_length=30)
    def __str__(self):
        return self.artist_name
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_name = models.CharField(max_length= 250)
    def __str__(self):
        return str(self.artist) + ', ' + str(self.album_name)
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    title = models.TextField()
    image = models.ImageField()
    audio_file = models.FileField()
    duration = models.CharField(max_length=20)
    paginate_by = 2
    def __str__(self):
        return str(self.album)+','+str(self.title)+','+str(self.audio_file)


# Create your models here.
