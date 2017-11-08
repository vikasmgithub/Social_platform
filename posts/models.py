from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
# Create your models here.


class Posts(models.Model):
    created_by = models.ForeignKey(User)
    title = models.TextField(max_length=100)
    content = models.TextField(max_length=100)
    slug = AutoSlugField(populate_from='title',unique=True)
    create_at = models.DateField(auto_now_add=True,null=False)
    update_at  = models.DateField(auto_now=True)

