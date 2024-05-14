"""
Module de tests d'intégration pour les profils utilisateurs.

Ce module contient des tests d'intégration pour les vues liées aux profils utilisateurs, y compris
la vérification
de l'affichage des pages d'index et de profil, du code de statut de la réponse, de l'utilisation
du bon template
et de la correspondance avec le profil utilisateur attendu.
"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfilesIntegrationTest(TestCase):
    """
    Classe de tests d'intégration pour les profils utilisateurs.
    """

    def setUp(self):
        """
        Initialisation des données de test.
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Pythonville')

    def test_index_page(self):
        """
        Teste l'affichage de la page d'index des profils.
        """
        url = reverse('profiles:profile_index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertContains(response, self.profile.user.username)

    def test_profile_page(self):
        """
        Teste l'affichage de la page de profil d'un utilisateur.
        """
        url = reverse('profiles:profile', args=[self.user.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertEqual(response.context['profile'], self.profile)
