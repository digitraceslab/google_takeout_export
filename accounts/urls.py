from django.urls import path
from django.contrib.auth.models import User

from . import views

urlpatterns = [
    path('profile/', views.UserProfileDetailView.as_view(), name='profile'),
]