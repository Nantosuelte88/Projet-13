from django.test import TestCase
from django.urls import reverse

class ProfilessIndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('profiles:profile_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
