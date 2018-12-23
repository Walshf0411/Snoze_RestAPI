from django.db import models
from Accounts.models import Snoze_User
# Create your models here.
class Song(models.Model):
    '''
        A basic song table representing the songs uploaded by the users of the App
    '''
    user_id = models.ForeignKey(Snoze_User, on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    duration = models.CharField(max_length=100)
    genere = models.CharField(max_length=100)
    label = models.CharField(max_length=100,default='no label')

class Album(models.Model):
    '''
        A basic album table
    '''
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100)

class Playlist(models.Model):
    '''
        Playlist table. private is boolean specifying whether the playlist is visiblie 
        publically or no.
    '''
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Snoze_User, on_delete=models.CASCADE)
    playlist_name = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=False)
    
class Like(models.Model):
    '''
        Entry in this table that represents that the user has liked the coresponding song.
    '''
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Snoze_User, on_delete = models.CASCADE)

'''class Comment(models.Model):
    song_id = models.ForeignKey(Songs, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Snoze_User, on_delete = models.CASCADE)
    comment = models.CharField(max_length=500)
    '''