from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import SignUp,edit_user

urlpatterns = [
    url(r'^signup/', SignUp.as_view() , name='signup'),
    url(r'^login/', auth_views.login, {'template_name':'login.html'} ,name='login'),
    url(r'^logout/', auth_views.logout, {'template_name':'logged_out.html'} ,name='logout'),
    url(r'^update/(?P<pk>[\-\w]+)/$', edit_user, name='account_update'),
]