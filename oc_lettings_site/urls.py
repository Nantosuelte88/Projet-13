"""
Définit les URL pour le site OC Lettings.

Ce module contient les URL du site OC Lettings, qui permettent de mapper les URL vers les vues
correspondantes.
Il ajoute également des chemins pour obtenir les fichiers statiques.
"""
from django.urls import re_path
from django.views.static import serve
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler404

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include(('lettings.urls', 'lettings'), namespace='lettings')),
    path('profiles/', include(('profiles.urls', 'profiles'), namespace='profiles')),
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

handler404 = 'oc_lettings_site.views.handler404'  # noqa
handler500 = 'oc_lettings_site.views.handler500'
