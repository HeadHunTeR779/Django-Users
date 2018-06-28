from django.db import models
from django.contrib.auth.models import User   #Built-in stuff: username email password firstname & lastname

# Create your models here.

class UserProfileInfo(models.Model):

    #take from built-in User we are gonna add our own fields in addition to fields already present in User
    user = models.OneToOneField(User)

    #My add-on fields
    portfolio_site = models.URLField(blank=True) #Not necessarily needed by user to fill it out
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True) #now we gotta make a folder profile_pics under media
    #install pillow in venv for python images


    def __str__(self):
        return self.user.username
