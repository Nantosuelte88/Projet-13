from django.test import TestCase
from django.urls import reverse

class LettingsIntegrationTest(TestCase):
    def test_index_page(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')