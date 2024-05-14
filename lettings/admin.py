"""
Ce module définit les classes d'administration pour l'application "lettings".
"""

from django.contrib import admin

from .models import Letting
from .models import Address

admin.site.register(Letting)
admin.site.register(Address)
