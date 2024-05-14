"""
Module de tests unitaires pour la gestion des erreurs 404.
"""

from django.test import TestCase, Client


class Handler404Tests(TestCase):
    """
    Classe de tests unitaires pour la gestion des erreurs 404.
    """

    def test_handler404(self):
        """
        Teste la gestion de l'erreur 404.
        """
        client = Client()
        response = client.get('/some-unknown-url/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'errors/404.html')
