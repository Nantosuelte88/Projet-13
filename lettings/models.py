"""
Ce module contient les modèles de l'application "lettings".
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Modèle représentant une adresse.

    Attributes:
        number (PositiveIntegerField): Numéro de rue (doit être inférieur ou égal à 9999).
        street (CharField): Nom de rue (max. 64 caractères).
        city (CharField): Nom de la ville (max. 64 caractères).
        state (CharField): Code de l'état (2 caractères, doit être supérieur ou égal à
        2 caractères).
        zip_code (PositiveIntegerField): Code postal (doit être inférieur ou égal à 99999).
        country_iso_code (CharField): Code ISO du pays (3 caractères, doit être supérieur ou égal
        à 3 caractères).

    Meta:
        verbose_name_plural: Nom pluriel utilisé dans l'administration.

    Methods:
        __str__: Représentation sous forme de chaîne de caractères de l'adresse.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        """
        Représentation sous forme de chaîne de caractères de l'adresse.
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Modèle représentant une location.

    Attributes:
        title (CharField): Titre de la location (max. 256 caractères).
        address (OneToOneField): Référence à l'objet Address associé.

    Methods:
        __str__: Représentation sous forme de chaîne de caractères de la location.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Représentation sous forme de chaîne de caractères de la location.
        """
        return self.title
