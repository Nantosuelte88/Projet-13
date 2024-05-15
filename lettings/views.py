"""
Ce module contient les vues pour l'application "lettings".
"""

import logging
from django.shortcuts import render
from .models import Letting
from sentry_sdk import capture_exception

logger = logging.getLogger(__name__)

# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit. Sed non placerat
# massa. Integer est nunc, pulvinar a
# tempor et, bibendum id arcu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices
# posuere cubilia curae; Cras eget scelerisque


def index(request):
    """
    Vue pour afficher la liste des locations.

    Args:
        request (HttpRequest): Objet représentant la requête HTTP reçue.

    Returns:
        HttpResponse: Réponse HTTP avec la liste des locations rendue dans le template
        "lettings/index.html".

    Raises:
        Exception: En cas d'erreur lors de l'affichage de la liste des locations.

    Notes:
        Cette vue utilise un bloc try-except pour capturer les exceptions qui pourraient se
        produire lors de l'affichage de la liste des locations. En cas d'erreur, l'exception
        est enregistrée dans les journaux et capturée par Sentry pour une gestion ultérieure.
    """
    try:
        lettings_list = Letting.objects.all()
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)
    except Exception as e:
        logger.error(
            "Une erreur s'est produite lors de l'affichage de la liste des locations : %s", str(e))
        capture_exception(e)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta nisl id
# eleifend. Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu, vitae
# efficitur
#  lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas auctor, est ut
# luctus congue, dui enim mattis enim, ac condimentum velit libero in magna. Suspendisse potenti.
# In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum. Ut quis urna pellentesque justo mattis
# ullamcorper ac non tellus. In tristique mauris eu velit fermentum, tempus pharetra est luctus.
# Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus. Mauris condimentum
# auctor elementum. Donec quis nisi ligula. Integer vehicula tincidunt enim, ac lacinia augue
# pulvinar sit amet.
def letting(request, letting_id):
    """
    Vue pour afficher les détails d'une location spécifique.

    Args:
        request (HttpRequest): Objet représentant la requête HTTP reçue.
        letting_id (int): Identifiant de la location à afficher.

    Returns:
        HttpResponse: Réponse HTTP avec les détails de la location rendus dans le template
        "lettings/letting.html".

    Raises:
        Letting.DoesNotExist: Si la location avec l'ID spécifié n'existe pas.
        Exception: En cas d'erreur lors de l'affichage des détails de la location.

    Notes:
        Cette vue utilise un bloc try-except pour capturer les exceptions qui pourraient se
        produire lors de l'affichage des détails de la location. En cas d'erreur, l'exception
        est enregistrée dans les journaux et capturée par Sentry pour une gestion ultérieure.
    """
    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Letting.DoesNotExist:
        logger.warning("La location avec l'ID %s n'a pas été trouvée.", letting_id)
    except Exception as e:
        logger.error(
            "Une erreur s'est produite lors de l'affichage des détails de la location : %s", str(e)
            )
        capture_exception(e)
