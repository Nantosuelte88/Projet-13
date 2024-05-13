from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile

class ProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Test City')

    def test_profile_view(self):
        url = reverse('profiles:profile', args=['testuser'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertEqual(response.context['profile'], self.profile)
        self.assertContains(response, 'testuser')
        self.assertContains(response, 'Test City')