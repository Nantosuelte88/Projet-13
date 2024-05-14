"""
Module de tests unitaires pour la vue d'index des profils utilisateurs.
"""

from django.test import TestCase
from django.urls import reverse


class ProfilesIndexViewTest(TestCase):
    """
    Classe de tests unitaires pour la vue d'index des profils utilisateurs.
    """

    def test_index_view(self):
        """
        Teste la vue d'index des profils utilisateurs.
        """
        response = self.client.get(reverse('profiles:profile_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
