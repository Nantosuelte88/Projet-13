"""
Module de tests d'intégration pour les fonctionnalités du package lettings.

Ce module contient des tests d'intégration pour les différentes fonctionnalités du package
lettings,
telles que la liste des locations et l'affichage d'une location spécifique.
"""
from django.test import TestCase
from django.urls import reverse

from lettings.models import Letting, Address


class LettingsIntegrationTest(TestCase):
    """
    Classe de tests d'intégration pour les fonctionnalités du package lettings.

    Cette classe contient des tests d'intégration pour les différentes fonctionnalités du
    package lettings,
    telles que la liste des locations et l'affichage d'une location spécifique.
    """

    def setUp(self):
        """
        Méthode de configuration des tests.

        Cette méthode est exécutée avant chaque test et permet de configurer les données
        nécessaires.
        """
        self.address = Address.objects.create(
            number=123, street="Rue de Python", city="Django", state="DJ", zip_code=12345,
            country_iso_code="PYT")
        self.letting = Letting.objects.create(title="Super Appartement", address=self.address)

    def test_list_lettings(self):
        """
        Test de la liste des locations.

        Ce test vérifie que la liste des locations est correctement affichée en vérifiant
        le code de réponse,
        le template utilisé et la présence de la location dans le contexte de la réponse.
        """
        response = self.client.get(reverse('lettings:letting_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertIn(self.letting, response.context['lettings_list'])

    def test_view_letting(self):
        """
        Test de l'affichage d'une location spécifique.

        Ce test vérifie que l'affichage d'une location spécifique est correct en vérifiant le code
        de réponse,
        le template utilisé, le titre de la location et l'adresse de la location affichée.
        """
        url = reverse('lettings:letting', args=[self.letting.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertEqual(response.context['title'], self.letting.title)
        self.assertEqual(str(response.context['address']), '123 Rue de Python')
