from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile

class ProfilesIntegrationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Pythonville')

    def test_index_page(self):
        url = reverse('profiles:profile_index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertContains(response, self.profile.user.username)

    def test_profile_page(self):
        url = reverse('profiles:profile', args=[self.user.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertEqual(response.context['profile'], self.profile)