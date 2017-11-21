from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.shortcuts import reverse
# Create your models here.


class Posts(models.Model):
    created_by = models.ForeignKey(User,related_name='post')
    title = models.TextField(max_length=100)
    content = models.TextField(max_length=100)
    slug = AutoSlugField(populate_from='title',unique=True)
    like = models.ManyToManyField(User,related_name='likes')
    create_at = models.DateField(auto_now_add=True,null=False)
    update_at  = models.DateField(auto_now=True)



    def __str__(self):
        return f'{self.created_by} asked {self.title}'



    @property
    def total_likes(self):

        return self.like.count()

    def get_absolute_url(self):
        return reverse('post:post')



