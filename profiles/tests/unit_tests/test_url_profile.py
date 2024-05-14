"""
Module de tests unitaires pour les URLs de profil utilisateur.
"""

from django.test import SimpleTestCase
from django.urls import reverse


class ProfileURLTest(SimpleTestCase):
    """
    Classe de tests unitaires pour les URLs de profil utilisateur.
    """

    def test_profile_url_resolves(self):
        """
        Teste la résolution de l'URL de profil utilisateur.
        """
        url = reverse('profiles:profile', args=['testuser'])
        self.assertEqual(url, '/profiles/testuser/')
