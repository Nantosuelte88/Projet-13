from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.template.loader import get_template

from oc_lettings_site.views import handler500

class ErrorViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_500_view(self):
        request = self.factory.get(reverse('index'))
        response = handler500(request)

        self.assertEqual(response.status_code, 500)
        
        template = get_template('errors/500.html')
        rendered_template = template.render()
        
        self.assertIn(rendered_template, response.content.decode())
        