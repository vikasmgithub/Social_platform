from django.shortcuts import render
from django.views import generic
from .models import Posts
from .foms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
# Create your views here.


class PostCreate(LoginRequiredMixin,generic.CreateView):
    login_url = reverse_lazy('user:login')
    template_name = 'userdashboard.html'
    model = Posts
    form_class  = PostForm

    def form_valid(self, form):
        form.instance.created_by =  self.request.user
        return super(PostCreate,self).form_valid(form)


class PostListView(LoginRequiredMixin,generic.ListView):
    login_url = reverse_lazy('user:login')
    template_name = 'feed.html'
    model = Posts


    def get_queryset(self,**kwargs):
        queryset = Posts.objects.all()
        return super(PostListView,self).get_queryset(**kwargs)

class PostDetailView(LoginRequiredMixin,generic.DetailView):
    login_url = reverse_lazy('user:login')
    template_name = 'detailview.html'
    model = Posts




def add_like(request):
    post_id = None

    if request.method == 'GET':
        post_id = request.GET["post_id"]

    likes = 0
    post = Posts.objects.get(id=(int(post_id)))
    if post:
        if request.user.post.like:
            likes = post.like - 1
        else:
            likes =post.like + 1
        post.like = likes
        post.save()

    return HttpResponse(likes)






