"""
Ce module définit les classes d'administration pour l'application "profiles".
"""


from django.contrib import admin

from .models import Profile

admin.site.register(Profile)
