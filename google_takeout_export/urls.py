"""
URL configuration for google_takeout_export project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from accounts.views import register as accounts_register
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', accounts_register, name='register'),
    path('instructions/', views.instructions, name='instructions'),
    path('privacy_notice/', views.privacy_notice, name='privacy_notice'),
    path('accounts/', include('accounts.urls')),
    path('api/takeout_items/', views.get_takeout_items, name='get_takeout_items_default'),
    path('api/takeout_items/<str:study_id>/', views.get_takeout_items, name='get_takeout_items'),
]
