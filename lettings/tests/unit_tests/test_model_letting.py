"""
Module de tests unitaires pour le modèle Letting.
"""
from django.test import TestCase
from lettings.models import Address, Letting


class LettingModelTest(TestCase):
    """
    Classe de tests unitaires pour le modèle Letting.
    """

    def test_letting_str_representation(self):
        """
        Teste la représentation en chaîne de caractères de la location.
        """
        address = Address(number=123, street='Rue Principale', city='Ville',
                          state='FR', zip_code=12345, country_iso_code='FRA')
        letting = Letting(title='My Letting', address=address)
        self.assertEqual(str(letting), 'My Letting')
