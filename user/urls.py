from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import SignUp,updateinfo,Profile,LoginRedirect

urlpatterns = [
    url(r'^signup/', SignUp.as_view() , name='signup'),
    url(r'^redirect/$', LoginRedirect.as_view(), name='redirect'),
    url(r'^login/', auth_views.login, {'template_name':'login.html'} ,name='login'),
    url(r'^logout/', auth_views.logout, {'template_name':'logged_out.html'} ,name='logout'),
    url(r'^update/(?P<id>[0-9]+)/$', updateinfo, name='account_update'),
    url(r'^(?P<slug>[\-\w]+)/$', Profile.as_view(), name='profile'),

]