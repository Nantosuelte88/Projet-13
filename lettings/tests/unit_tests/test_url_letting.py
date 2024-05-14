"""
Module de tests unitaires pour l'URL d'une location spécifique.
"""
from django.test import TestCase
from django.urls import resolve, reverse
from lettings.views import letting


class LettingURLTest(TestCase):
    """
    Classe de tests unitaires pour l'URL d'une location spécifique.
    """

    def test_letting_url_resolves(self):
        """
        Teste la résolution de l'URL vers la vue correspondante.
        """
        url = reverse('lettings:letting', args=[1])
        resolved_view = resolve(url).func
        self.assertEqual(resolved_view, letting)
