from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView

from .models import User
from . import forms


class UserProfileDetailView(DetailView):
    model = User
    template_name = 'accounts/profile.html'

    def get_object(self):
        return self.request.user


@method_decorator(login_required, name='dispatch')
class ConsentView(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'accounts/consent_form.html'
    success_url = '/accounts/profile/'
    form_class = forms.ConsentForm
    success_message = "Your consent has been registered succesfully"

    def get_success_url(self):
        return '/accounts/profile/'

    def get_object(self):
        return self.request.user
    