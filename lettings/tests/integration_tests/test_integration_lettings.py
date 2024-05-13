from django.test import TestCase
from django.urls import reverse

from lettings.models import Letting, Address


class LettingsIntegrationTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(number=123, street="Rue de Python", city="Django", state="DJ", zip_code=12345, country_iso_code="PYT")
        self.letting = Letting.objects.create(title="Super Appartement", address=self.address)

    def test_list_lettings(self):
        response = self.client.get(reverse('lettings:letting_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        self.assertIn(self.letting, response.context['lettings_list'])

    def test_view_letting(self):
        url = reverse('lettings:letting', args=[self.letting.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertEqual(response.context['title'], self.letting.title)
        self.assertEqual(str(response.context['address']), '123 Rue de Python')