from django.test import TestCase
from lettings.models import Address, Letting



class LettingModelTest(TestCase):
    def test_letting_str_representation(self):
        address = Address(number=123, street='Rue Principale', city='Ville', state='FR', zip_code=12345, country_iso_code='FRA')
        letting = Letting(title='My Letting', address=address)
        self.assertEqual(str(letting), 'My Letting')
        