"""Social_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from user import urls as userurls
from posts import urls as posturls
from .views import profile
from connections import  urls as connectionurls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', profile,name='home'),
    url(r'^user/', include(userurls, namespace='user')),
    url(r'^post/', include(posturls, namespace='post')),
    url(r'^connectionurl/', include(connectionurls, namespace='post')),

]
