from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles.views import index

class ProfilesURLTest(SimpleTestCase):
    def test_profile_index_url(self):
        url = reverse('profiles:profile_index')
        self.assertEqual(resolve(url).func, index)