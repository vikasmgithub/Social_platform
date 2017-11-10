from django.conf.urls import url
from .views import PostCreate,PostListView,PostDetailView,add_like

urlpatterns = [
    url(r'^createpost/$', PostCreate.as_view() , name='post'),
    url(r'^feed/$', PostListView.as_view() , name='feed'),
    url(r'add_like/$', add_like, name='add_like'),
    url(r'^feed/(?P<slug>[\w-]+)/$', PostDetailView.as_view() , name='detail'),
]