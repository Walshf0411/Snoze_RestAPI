from django.db import models
from django.contrib.auth.models import User
from Songs.models import Song, Playlist
# Create your models here.
# User class is the default django user model which proviudes authentication and other features
class Snoze_User(User):
    '''
        A Model class that has all the features of the built-in django User model 
        and also includes a phone_number field.
        This is the main table that will be used for user registration.
        Any includes to be made to the users of the app should be made here.
    '''
    phone_number = models.CharField(max_length=10, unique=True)
    profile_picture = models.ImageField() 
    private = models.BooleanField(default=False)


class Subscribe(models.Model):
    '''
        A model that represents whether a user has subscribed to the private plan.
    '''
    user_id = models.ForeignKey(Snoze_User, on_delete=models.CASCADE)  
    start_date = models.DateField(auto_now_add=True)    
    end_date = models.DateField()

class UserRelation(models.Model):
    '''
        A model that shows the relationship between two user.
        Followed is the user that is being followed 
        follower is the user that follows the followed user
    '''
    followed = models.ForeignKey(Snoze_User, on_delete=models.CASCADE)
    follower = models.ForeignKey(Snoze_User, on_delete=models.CASCADE)

class Blocked(models.Model):
    '''
        An entry in this table would represent that the 'blocked' user 
        has been blocked by the 'blocker' user
    '''
    blocked = models.ForeignKey(Snoze_User, on_delete=models.CASCADE)
    blocker = models.ForeignKey(Snoze_User, on_delete=models.CASCADE)

class Recent(models.Model):
    '''
        This table is like a stack for the users. A song played by the user would first be checked for 
        in this table, if not found an entry would be made in this table else the song field from this 
        table would be retrieved and the time would be retrieved.
        Also the table would delete the songs that the is has the minimum value in the last_played
        when the decided limit for the recent songs is reached. (for premium users there will be no limit)
    '''
    user_id = models.ForeignKey(Snoze_User, on_delete=models.CASCADE)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    last_played = models.DateTimeField(auto_now=True) 


class Favourite_Playlist(models.Model):
    '''
        An entry in this table represents that the user has favourted the corresponding playlist
    '''
    user_id = models.ForeignKey(Snoze_User, on_delete=models.CASCADE)
    playlist_id = models.ForeignKey(Playlist, on_delete=models.CASCADE)

class Favourite_Song(models.Model):
    '''
        An entry in this table represents that the user has favourted the corresponding playlist
    '''
    user_id = models.ForeignKey(Snoze_User, on_delete=models.CASCADE)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)