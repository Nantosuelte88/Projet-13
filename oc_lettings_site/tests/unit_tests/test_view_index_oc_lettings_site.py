"""
Module de tests unitaires pour la vue d'index.
"""

from django.test import TestCase, Client
from django.urls import reverse


class IndexViewTest(TestCase):
    """
    Classe de tests unitaires pour la vue d'index.
    """

    def setUp(self):
        """
        Initialisation des données de test.
        """
        self.client = Client()

    def test_index_view(self):
        """
        Teste l'affichage de la vue d'index.
        """
        url = reverse('index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
