from django.conf.urls import url
from . import views

app_name = 'vranaya_app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^albums$', views.albums, name='albums'),

    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    
    url(r'^create_album/$', views.create_album, name='create_album'),
    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),

    url(r'^videos/(?P<video_id>[0-9]+)/detail/$', views.detail_video, name='detail_video'),
    url(r'^videos/(?P<filter_by>[a-zA_Z0-9]+)/$', views.videos, name='videos'),
    url(r'^create_video/$', views.create_video, name='create_video'),
    url(r'^videos/(?P<video_id>[0-9]+)/delete_video/$', views.delete_video, name='delete_video'),


]
