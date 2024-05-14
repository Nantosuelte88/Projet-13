"""
Module de tests unitaires pour la gestion des erreurs 500.
"""

from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.template.loader import get_template

from oc_lettings_site.views import handler500


class ErrorViewTest(TestCase):
    """
    Classe de tests unitaires pour la gestion des erreurs 500.
    """

    def setUp(self):
        """
        Initialisation des données de test.
        """
        self.factory = RequestFactory()

    def test_500_view(self):
        """
        Teste la gestion de l'erreur 500.
        """
        request = self.factory.get(reverse('index'))
        response = handler500(request)

        self.assertEqual(response.status_code, 500)

        template = get_template('errors/500.html')
        rendered_template = template.render()

        self.assertIn(rendered_template, response.content.decode())
