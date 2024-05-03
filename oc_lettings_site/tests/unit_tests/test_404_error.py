from django.test import TestCase, Client

class Handler404Tests(TestCase):
    def test_handler404(self):
        client = Client()
        response = client.get('/some-unknown-url/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'errors/404.html')
