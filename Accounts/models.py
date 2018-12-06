from django.db import models
from django.contrib.auth.models import User

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