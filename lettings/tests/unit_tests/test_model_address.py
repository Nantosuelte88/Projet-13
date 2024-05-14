"""
Module de tests unitaires pour le modèle Address.
"""
from django.test import TestCase
from lettings.models import Address


class AddressModelTest(TestCase):
    """
    Classe de tests unitaires pour le modèle Address.
    """

    def test_address_str_representation(self):
        """
        Teste la représentation en chaîne de caractères de l'adresse.
        """
        address = Address(number=123, street='Rue Principale', city='Ville',
                          state='FR', zip_code=12345, country_iso_code='FRA')
        self.assertEqual(str(address), '123 Rue Principale')

    def test_address_meta_verbose_name_plural(self):
        """
        Teste le champ verbose_name_plural de l'adresse.
        """
        self.assertEqual(Address._meta.verbose_name_plural, 'Addresses')
