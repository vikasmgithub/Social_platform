from django.forms import ModelForm
from .models import Posts


class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields =['title','content']





