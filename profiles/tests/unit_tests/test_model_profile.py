from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Test City')

    def test_profile_str(self):
        self.assertEqual(str(self.profile), 'testuser')