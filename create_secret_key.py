"""Genere une clé secrete indispensable à la gestion de Django"""
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
