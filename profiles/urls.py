"""
Ce module définit les URL pour l'application "profiles".
"""

from django.urls import path

from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='profile_index'),
    path('<str:username>/', views.profile, name='profile'),
]
