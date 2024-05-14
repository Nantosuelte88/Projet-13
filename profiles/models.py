"""
Ce module contient les modèles de l'application "profiles".
"""


from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Modèle pour les profils utilisateur.

    Ce modèle représente le profil d'un utilisateur, associé à un modèle User via une relation
    OneToOneField.
    Il contient également un champ pour la ville préférée de l'utilisateur.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles_profile')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Méthode pour représenter le profil sous forme de chaîne de caractères; renvoie le nom
        d'utilisateur de l'utilisateur associé au profil.
        """
        return self.user.username
