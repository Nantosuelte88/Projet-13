"""
Module de tests unitaires pour les URLs des profils utilisateurs.
"""

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles.views import index


class ProfilesURLIndexTest(SimpleTestCase):
    """
    Classe de tests unitaires pour les URLs des profils utilisateurs.
    """

    def test_profile_index_url(self):
        """
        Teste l'URL de la page d'index des profils.
        """
        url = reverse('profiles:profile_index')
        self.assertEqual(resolve(url).func, index)
