"""
Ce module définit les URL pour l'application "lettings".
"""

from django.urls import path
from . import views

app_name = 'lettings'

urlpatterns = [
    path('', views.index, name='letting_index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
