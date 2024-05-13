from django.test import TestCase
from django.urls import reverse

class LettingsIndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('lettings:letting_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
