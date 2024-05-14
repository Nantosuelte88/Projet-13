"""
Module de tests unitaires pour le modèle de profil utilisateur.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileModelTest(TestCase):
    """
    Classe de tests unitaires pour le modèle de profil utilisateur.
    """

    def setUp(self):
        """
        Initialisation des données de test.
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Test City')

    def test_profile_str(self):
        """
        Teste la méthode __str__ du modèle de profil utilisateur.
        """
        self.assertEqual(str(self.profile), 'testuser')
