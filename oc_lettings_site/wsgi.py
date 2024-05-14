"""
Fichier WSGI pour le site OC Lettings.

Ce fichier configure l'application WSGI (Web Server Gateway Interface) pour le déploiement du site
OC Lettings.
Il définit également les paramètres d'environnement pour les paramètres Django spécifiques à ce
projet.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_wsgi_application()
