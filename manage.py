"""
Script de gestion pour le projet OC Lettings.

Ce script est utilisé pour gérer différentes tâches de gestion du projet OC Lettings,
telles que le démarrage du serveur de développement Django et l'exécution des commandes
de gestion Django.
Il définit également les paramètres d'environnement pour les paramètres Django spécifiques
à ce projet.
"""

import os
import sys


def main():
    """
    Fonction principale du script manage.py.

    Cette fonction définit les paramètres d'environnement pour les paramètres Django spécifiques
    à ce projet
    et exécute les commandes de gestion Django à partir de la ligne de commande.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# Ajout d'une ligne pour tester le webhook
