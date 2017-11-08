from django.conf.urls import url
from .views import PostCreate,PostListView

urlpatterns = [
    url(r'^createpost/$', PostCreate.as_view() , name='post'),
    url(r'^feed/$', PostListView.as_view() , name='feed'),
    url(r'^feed/(?P<slug>[\w-]+)/$', PostListView.as_view() , name='detail'),
]