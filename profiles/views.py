"""
Ce module contient les vues pour l'application "profiles".
"""


from django.shortcuts import render
from .models import Profile

# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d


def index(request):
    """
    Vue pour la page d'accueil des profils.

    Cette vue récupère tous les profils enregistrés dans la base de données et les passe au
    template 'profiles/index.html'.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)

# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt,
# dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et netus
# et males


def profile(request, username):
    """
    Vue pour l'affichage d'un profil individuel.

    Cette vue récupère le profil correspondant à l'utilisateur avec le nom d'utilisateur
    spécifié et le passe au template 'profiles/profile.html'.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
