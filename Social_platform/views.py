from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from user.models import UserProfile
# Create your views here.

def profile(request):
    user=request.user
    profile = UserProfile.objects.get(user=user)
    slug = profile.slug
    return redirect(reverse_lazy('user:profile', kwargs={'slug':slug}))
