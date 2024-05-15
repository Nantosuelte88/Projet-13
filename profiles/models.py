"""
Ce module contient les modèles de l'application "profiles".
"""


from django.db import models
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)


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

    def save(self, *args, **kwargs):
        """
        Méthode pour enregistrer le profil. Enregistre également les informations de l'événement
        dans les journaux et capture les exceptions avec Sentry si nécessaire.
        """
        logger.info(f"Enregistrement du profil de l'utilisateur {self.user.username}")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        Méthode pour supprimer le profil. Enregistre également les informations de l'événement
        dans les journaux et capture les exceptions avec Sentry si nécessaire.
        """
        logger.info(f"Suppression du profil de l'utilisateur {self.user.username}")
        super().delete(*args, **kwargs)
