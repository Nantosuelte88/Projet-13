Structure de la base de données et des modèles
==============================================

La base de données est structurée comme suit :

- **Profile** : Représente les utilisateurs de l'application.
- **Letting** : Représente les annonces de location.
- **Address** : Contient les adresses des biens immobiliers.

Exemple de modèle :

.. code-block:: python

    from django.db import models
    from django.core.validators import MaxValueValidator, MinLengthValidator
    import logging

    logger = logging.getLogger(__name__)

    class Address(models.Model):
        number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
        street = models.CharField(max_length=64)
        city = models.CharField(max_length=64)
        state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
        zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
        country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

        def save(self, *args, **kwargs):
            logger.info("Enregistrement de l'adresse : %s", str(self))
            super().save(*args, **kwargs)

        def delete(self, *args, **kwargs):
            logger.info("Suppression de l'adresse : %s", str(self))
            super().delete(*args, **kwargs)

        class Meta:
            verbose_name_plural = "Addresses"

        def __str__(self):
            return f'{self.number} {self.street}'


    class Letting(models.Model):
        title = models.CharField(max_length=256)
        address = models.OneToOneField(Address, on_delete=models.CASCADE)

        def save(self, *args, **kwargs):
            logger.info("Enregistrement de la location : %s", str(self))
            super().save(*args, **kwargs)

        def delete(self, *args, **kwargs):
            logger.info("Suppression de la location : %s", str(self))
            super().delete(*args, **kwargs)

        def __str__(self):
            return self.title
