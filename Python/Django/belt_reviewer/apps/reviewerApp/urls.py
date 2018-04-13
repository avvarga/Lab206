from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^books$', views.books),
    url(r'^books/add$', views.add_new),
    url(r'^books/(?P<id>\d+)$', views.reviews),
]