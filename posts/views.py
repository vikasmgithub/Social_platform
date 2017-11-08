from django.shortcuts import render
from django.views import generic
from .models import Posts
from .foms import PostForm
# Create your views here.


class PostCreate(generic.CreateView):
    template_name = 'userdashboard.html'
    model = Posts
    form_class  = PostForm

    def form_valid(self, form):
        form.instance.created_by =  self.request.user
        return super(PostCreate,self).form_valid(form)


class PostListView(generic.ListView):
    template_name = 'feed.html'
    model = Posts


    def get_queryset(self,**kwargs):
        queryset = Posts.objects.all()
        return super(PostListView,self).get_queryset(**kwargs)

class PostDetailView(generic.DetailView):
    template_name = 'detail.html'
    model = Posts





