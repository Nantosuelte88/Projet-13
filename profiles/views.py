"""
Ce module contient les vues pour l'application "profiles".
"""

from django.shortcuts import render
from .models import Profile
import logging
from sentry_sdk import capture_exception

logger = logging.getLogger(__name__)

# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d


def index(request):
    """
    Vue pour la page d'accueil des profils.

    Args:
        request (HttpRequest): Objet représentant la requête HTTP reçue.

    Returns:
        HttpResponse: Réponse HTTP avec la liste des profils rendue dans le template
        "profiles/index.html".

    Raises:
        Exception: En cas d'erreur lors de l'accès à la page d'accueil des profils.

    Notes:
        Cette vue utilise un bloc try-except pour capturer les exceptions qui pourraient se
        produire lors de l'accès à la page d'accueil des profils. En cas d'erreur, l'exception
        est enregistrée dans les journaux et capturée par Sentry pour une gestion ultérieure.
    """
    logger.info("Accès à la page d'accueil des profils")
    try:
        profiles_list = Profile.objects.all()
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)
    except Exception as e:
        logger.error(f"Erreur lors de l'accès à la page d'accueil des profils: {str(e)}")
        capture_exception(e)

# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt,
# dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et netus
# et males


def profile(request, username):
    """
    Vue pour l'affichage d'un profil individuel.

    Args:
        request (HttpRequest): Objet représentant la requête HTTP reçue.
        username (str): Nom d'utilisateur du profil à afficher.

    Returns:
        HttpResponse: Réponse HTTP avec le profil rendu dans le template "profiles/profile.html".

    Raises:
        Profile.DoesNotExist: Si le profil de l'utilisateur spécifié n'existe pas.
        Exception: En cas d'erreur lors de l'accès au profil de l'utilisateur.

    Notes:
        Cette vue utilise un bloc try-except pour capturer les exceptions qui pourraient se
        produire lors de l'accès au profil de l'utilisateur. En cas d'erreur, l'exception est
        enregistrée dans les journaux et capturée par Sentry pour une gestion ultérieure.
    """
    logger.info(f"Accès au profil de l'utilisateur {username}")
    try:
        profile = Profile.objects.get(user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Profile.DoesNotExist:
        logger.warning(f"Profil de l'utilisateur {username} introuvable")
        # Rediriger vers une page d'erreur ???   A MODIFIER
    except Exception as e:
        logger.error(f"Erreur lors de l'accès au profil de l'utilisateur {username}: {str(e)}")
        capture_exception(e)
