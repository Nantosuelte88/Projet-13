from django.test import SimpleTestCase
from django.urls import reverse

class ProfileURLTest(SimpleTestCase):
    def test_profile_url_resolves(self):
        url = reverse('profiles:profile', args=['testuser'])
        self.assertEqual(url, '/profiles/testuser/')
        