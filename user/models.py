from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name='user')
    bio = models.TextField(default='',blank=True)
    phone = models.CharField(max_length=13,blank=True,default='')
    city = models.TextField(max_length=50,blank=True,default='')


    def create_profile(sender,**kwargs):
        user = kwargs["instance"]
        if kwargs["created"]:
            user_profile = UserProfile(user=user)
            user_profile.save()

    post_save.connect(create_profile,sender=User)
