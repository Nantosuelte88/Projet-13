from lettings.models import Letting, Address

from django.test import TestCase
from django.urls import reverse

from lettings.views import index, letting

class LettingsViewTest(TestCase):
    def test_letting_view(self):
        address = Address.objects.create(number=123, street='Test Street', city='Test City',
                                         state='TS', zip_code=12345, country_iso_code='TST')
        letting = Letting.objects.create(title='Test Letting', address=address)
        response = self.client.get(reverse('lettings:letting', args=(letting.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertContains(response, 'Test Letting')