"""
Ce module définit la configuration de l'application OC Lettings.

La classe `OCLettingsSiteConfig` hérite de `AppConfig` et est utilisée pour configurer
l'application OC Lettings.
"""

from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    """
    Classe de configuration de l'application OC Lettings.

    Attributes:
        name (str): Nom de l'application.
    """
    name = 'oc_lettings_site'
