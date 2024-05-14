"""
Module de tests unitaires pour la vue de l'index des locations.
"""
from django.test import TestCase
from django.urls import reverse


class LettingsIndexViewTest(TestCase):
    """
    Classe de tests unitaires pour la vue de l'index des locations.
    """

    def test_index_view(self):
        """
        Teste la vue de l'index des locations.
        """
        response = self.client.get(reverse('lettings:letting_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
