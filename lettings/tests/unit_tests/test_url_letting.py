from django.test import TestCase
from django.urls import resolve, reverse
from lettings.views import letting

class LettingURLTest(TestCase):
    def test_letting_url_resolves(self):
        url = reverse('lettings:letting', args=[1])  
        resolved_view = resolve(url).func
        # Vérifier si la vue résolue est bien la fonction "letting"
        self.assertEqual(resolved_view, letting)