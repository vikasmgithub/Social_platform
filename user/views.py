from django.views import generic

# from .forms import UserForm
from django.forms.models import inlineformset_factory
from .forms import SignUpForm

from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from .models import UserProfile
from posts.models import Posts


from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.


class LoginRedirect(generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        profile = UserProfile.objects.get(user=user)
        slug = profile.slug
        print(slug)
        return reverse('user:profile', kwargs={'slug':slug})





class SignUp(generic.CreateView):
    template_name = 'register.html'
    form_class = SignUpForm
    success_url = '/'


class Profile(LoginRequiredMixin,generic.DetailView):
    template_name = 'profile.html'

    def get_object(self):
        username = self.kwargs.get("slug")
        if username is None:
            raise Http404
        obj=get_object_or_404(UserProfile,slug=username)
        print(obj)
        return obj

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context["posts"] = Posts.objects.filter(created_by=self.request.user)
        return context

# @login_required() # only logged in users should access this
# def edit_user(request,pk):
#     # querying the User object with pk from url
#     # pk = request.user.pk
#     user = User.objects.get(pk=pk)
#
#     # prepopulate UserProfileForm with retrieved user values from above.
#     user_form = UserForm(instance=user)
#
#     # The sorcery begins from here, see explanation below
#     ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('bio', 'phone', 'city'))
#     formset = ProfileInlineFormset(instance=user)
#
#     if request.user.is_authenticated() and request.user.id == user.id:
#         if request.method == "POST":
#             user_form = UserForm(request.POST, request.FILES, instance=user)
#             formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
#
#             if user_form.is_valid():
#                 created_user = user_form.save(commit=False)
#                 formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
#
#                 if formset.is_valid():
#                     created_user.save()
#                     formset.save()
#                     return HttpResponseRedirect('/accounts/profile/')
#
#         return render(request, "account_update.html", {
#             "noodle": pk,
#             "noodle_form": user_form,
#             "formset": formset,
#         })
#     else:
#         raise PermissionDenied
# @login_required() # only logged in users should access this
# def edit_user(request):
#     # querying the User object with pk from url
#     # pk = request.user.pk
#     user = request.user
#
    # profile = UserProfile.objects.get(user=user)
    # slug = profile.slug
#
#     # prepopulate UserProfileForm with retrieved user values from above.
#     user_form = UserForm(instance=user)
#
#     # The sorcery begins from here, see explanation below
#     ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('bio', 'phone', 'city'))
#     formset = ProfileInlineFormset(instance=user)
#
#     if request.user.is_authenticated() and request.user.id == user.id:
#         if request.method == "POST":
#             user_form = UserForm(request.POST, request.FILES, instance=user)
#             formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
#
#             if user_form.is_valid():
#                 created_user = user_form.save(commit=False)
#                 formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
#
#                 if formset.is_valid():
#                     created_user.save()
#                     formset.save()
#                     return reverse('user:profile', kwargs={'slug':slug})
#
        # return render(request, "account_update.html", {
        #     "noodle": slug,
        #     "noodle_form": user_form,
        #     "formset": formset,
        # })
#     else:
#         raise PermissionDenied

@login_required()
def updateinfo(request,id):

    user = User.objects.get(id=id)

    profile = UserProfile.objects.get(user=user)
    slug = profile.slug

    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('bio', 'phone', 'city'))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == 'POST':
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect(reverse('user:profile', kwargs={'slug':slug}))

        return render(request, "account_update.html", {
            "noodle": slug,
            "formset": formset,
        })



