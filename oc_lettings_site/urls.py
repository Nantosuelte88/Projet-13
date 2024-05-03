from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler404

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include(('lettings.urls', 'lettings'), namespace='lettings')),
    path('profiles/', include(('profiles.urls', 'profiles'), namespace='profiles')),
    path('admin/', admin.site.urls),
]

handler404 = 'oc_lettings_site.views.handler404'
handler500 = 'oc_lettings_site.views.handler500'
