"""
Fichier de vues pour le site OC Lettings.
"""

from django.shortcuts import render

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
    """
    return render(request, 'index.html')


def handler404(request, exception):
    """
    Gestionnaire d'erreur pour les erreurs 404; renvoie le template 'errors/404.html' avec le
    statut 404 lorsqu'une erreur 404 se produit.
    """
    return render(request, 'errors/404.html', status=404)


def handler500(request):
    """
    Gestionnaire d'erreur pour les erreurs 500; renvoie le template 'errors/500.html' avec le
    statut 500 lorsqu'une erreur 500 se produit.
    """
    return render(request, 'errors/500.html', status=500)
