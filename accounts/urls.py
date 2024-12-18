from django.urls import path

from . import views

urlpatterns = [
    path('profile/', views.UserProfileDetailView.as_view(), name='profile'),
    path('consent/', views.ConsentView.as_view(), name='consent'),
    path('withdraw_consent/', views.ConsentWithdrawView.as_view(), name='withdraw_consent'),
    path('upload_takeout/', views.GoogleTakeoutUploadView.as_view(), name='upload_takeout'),
]