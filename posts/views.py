from django.http import HttpResponse
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.shortcuts import render
from django.views import generic
from .models import Posts
from .foms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# Create your views here.


class PostCreate(LoginRequiredMixin,generic.CreateView):
    login_url = reverse_lazy('user:login')
    template_name = 'feed.html'
    model = Posts
    form_class  = PostForm

    def form_valid(self, form):
        form.instance.created_by =  self.request.user
        return super(PostCreate,self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostCreate, self).get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context


# class PostListView(LoginRequiredMixin,generic.ListView):
#     login_url = reverse_lazy('user:login')
#     template_name = 'feed.html'
#     model = Posts
#
#
#     def get_queryset(self,**kwargs):
#         queryset = Posts.objects.all()
#         return super(PostListView,self).get_queryset(**kwargs)



class PostDetailView(LoginRequiredMixin,generic.DetailView):
    login_url = reverse_lazy('user:login')
    template_name = 'detailview.html'
    model = Posts




@login_required
@require_POST
def like(request):
    if request.method == 'POST':
        user = request.user
        slug = request.POST.get('slug', None)
        post = get_object_or_404(Posts, slug=slug)

        if post.like.filter(id=user.id).exists():
            post.like.remove(user)
            message = 'You disliked this'
        else:
            post.like.add(user)
            message = 'You liked this'

    ctx = {'likes_count': post.total_likes, 'message': message}
    return HttpResponse(json.dumps(ctx), content_type='application/json')





