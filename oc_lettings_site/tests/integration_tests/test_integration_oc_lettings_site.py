"""
Module de tests d'intégration pour les pages d'index du site de location.
Ce module contient des tests d'intégration pour les pages d'index du site de location,
y compris la vérification du code de statut de la réponse et de l'utilisation du bon template.
"""
from django.test import TestCase
from django.urls import reverse


class LettingsIntegrationTest(TestCase):
    """
    Classe de tests d'intégration pour les pages d'index du site de location.
    """

    def test_index_page(self):
        """
        Teste l'affichage de la page d'index du site de location.
        """
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
