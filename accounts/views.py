import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from multiprocessing import Process

from .models import User
from . import forms


def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = forms.RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class ConsentWithdrawView(SuccessMessageMixin, UpdateView):
    model = User
    template_name = 'accounts/consent_withdraw_form.html'
    success_url = '/accounts/profile/'
    form_class = forms.ConsentWithdrawForm
    success_message = "Your consent has been withdrawn succesfully"

    def get_success_url(self):
        return '/accounts/profile/'
    
    def get_object(self):
        return self.request.user


@method_decorator(login_required, name='dispatch')
class GoogleTakeoutUploadView(View):
    form_class = forms.GoogleTakeoutUploadForm
    template_name = 'accounts/upload_takeout.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            if not os.path.exists(settings.MEDIA_ROOT):
                os.makedirs(settings.MEDIA_ROOT)
            file_path = os.path.join(settings.MEDIA_ROOT, file.name)
            with open(file_path, "wb") as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            messages.success(request, 'File uploaded successfully.')
            return redirect('profile')
        return render(request, self.template_name, {'form': form})
