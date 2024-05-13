from django.test import SimpleTestCase
from django.urls import reverse, resolve
from lettings.views import index

class LettingsURLTest(SimpleTestCase):
    def test_lettings_index_url(self):
        url = reverse('lettings:letting_index')
        self.assertEqual(resolve(url).func, index)