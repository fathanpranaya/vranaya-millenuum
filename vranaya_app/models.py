from django.contrib.auth.models import Permission, User
from django.db import models


class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    view_counter = models.IntegerField(default=1)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)
    view_counter = models.IntegerField(default=1)

    def __str__(self):
        return self.song_title

class Video(models.Model):
    user = models.ForeignKey(User, default=1)
    video_title = models.CharField(max_length=250)
    video_file = models.FileField(default='')
    video_logo = models.FileField(default='')
    view_counter = models.IntegerField(default=1)
    is_360 = models.BooleanField(default=False)

    def __str__(self):
        return self.video_title
