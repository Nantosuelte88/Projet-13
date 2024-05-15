"""
Fichier de vues pour le site OC Lettings.
"""

from django.shortcuts import render
import logging
from sentry_sdk import capture_exception

logger = logging.getLogger(__name__)

# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo
# consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis, sem mi
# convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget consequat ipsum
# lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis
# enim cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.


def index(request):
    """
    Vue pour la page d'accueil du site; renvoie le template 'index.html' pour afficher la page
    d'accueil du site.

    Returns:
        HttpResponse: Réponse HTTP avec le template 'index.html' rendu.

    Notes:
        Cette vue enregistre l'accès à la page d'accueil dans les journaux à l'aide du logger.
    """
    try:
        logger.info("Accès à la page d'accueil")
        return render(request, 'index.html')
    except Exception as e:
        logger.error("Une erreur s'est produite lors du rendu de la page d'accueil : %s", str(e))
        capture_exception(e)


def handler404(request, exception):
    """
    Gestionnaire d'erreur pour les erreurs 404; renvoie le template 'errors/404.html' avec le
    statut 404 lorsqu'une erreur 404 se produit.
    """
    logger.warning("Erreur 404 : Page non trouvée")
    return render(request, 'errors/404.html', status=404)


def handler500(request):
    """
    Gestionnaire d'erreur pour les erreurs 500; renvoie le template 'errors/500.html' avec le
    statut 500 lorsqu'une erreur 500 se produit.
    """
    logger.error("Erreur 500 : Erreur interne du serveur")
    return render(request, 'errors/500.html', status=500)
