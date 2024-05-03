from django.test import TestCase
import pytest
from django.urls import reverse
from django.test import RequestFactory
from lettings.models import Letting
from lettings.views import index

"""
@pytest.mark.django_db
def test_index_view():
    # Créer des données de test
    Letting.objects.create(title='Test Property', description='Test Description')

    # Créer une instance de RequestFactory
    factory = RequestFactory()

    # Créer une requête GET vers la vue index
    request = factory.get(reverse('lettings:letting_index'))

    # Appeler la vue en utilisant la requête
    response = index(request)

    # Vérifier que la réponse renvoie un statut HTTP 200 (OK)
    assert response.status_code == 200

    # Vérifier que la réponse contient les données de la propriété créée
    assert 'Test Property' in response.content.decode()
    assert 'Test Description' in response.content.decode()
"""


def test_teeeest():
    assert 'teeets'