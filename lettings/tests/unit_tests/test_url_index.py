"""
Module de tests unitaires pour l'URL de l'index des locations.
"""
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from lettings.views import index


class LettingsURLIndexTest(SimpleTestCase):
    """
    Classe de tests unitaires pour l'URL de l'index des locations.
    """

    def test_lettings_index_url(self):
        """
        Teste l'URL de l'index des locations.
        """
        url = reverse('lettings:letting_index')
        self.assertEqual(resolve(url).func, index)
