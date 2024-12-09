from django.urls import path

from . import views

urlpatterns = [
    path('profile/', views.UserProfileDetailView.as_view(), name='profile'),
    path('consent/', views.ConsentView.as_view(), name='consent'),
]