"""
Ce module configure l'interface ASGI pour le site OC Lettings.

Il utilise la fonction `get_asgi_application` pour obtenir l'application ASGI de Django
et définit la configuration de l'environnement Django.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_asgi_application()
