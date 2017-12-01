from django import forms
from django.contrib.auth.models import User

from .models import Album, Song, Video


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']
        widgets = {
            'artist': forms.TextInput(attrs={'class': 'form-control'}),
            'album_title': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.TextInput(attrs={'class': 'form-control'}),
            'album_logo': forms.FileInput(attrs={'class': 'form-control'}),
        }


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']
        widgets = {
            'song_title': forms.TextInput(attrs={'class': 'form-control'}),
            'audio_file': forms.FileInput(attrs={'class': 'form-control'}),
        }


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        



class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ['video_title', 'video_file', 'video_logo', 'is_360']
        widgets = {
            'video_title': forms.TextInput(attrs={'class': 'form-control'}),
            'video_file': forms.FileInput(attrs={'class': 'form-control'}),
            'video_logo': forms.FileInput(attrs={'class': 'form-control'}),
            'is_360': forms.CheckboxInput(attrs={'class': 'checkbox'}),
        }
