from django.test import TestCase, Client

from django.http import HttpResponseServerError
"""
class Handler500Tests(TestCase):
    def test_handler500(self):
        client = Client()
        response = client.get('/url-that-triggers-500/')
        self.assertEqual(response.status_code, 500)
        self.assertTemplateUsed(response, 'errors/500.html')

"""
