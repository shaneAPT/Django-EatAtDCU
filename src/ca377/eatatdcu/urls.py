from django.conf.urls import url

from . import views
app_name = 'eatatdcu'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^restaurants$', views.restaurants, name='restaurants'),
    url(r'^restaurants/specials/(?P<restaurant>[a-z0-9 ]+)$', views.specials, name='specials'),
    ]
