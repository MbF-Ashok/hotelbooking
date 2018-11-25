from django.conf.urls import url, include
from django.contrib import admin
from .views import home, register, reservation, reserv_table, create_table
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^register/', register),
    url(r'^reserve-bulktable/', reservation, name='reservation'),
    url(r'^Create-table/', create_table, name='create_table'),
    url(r'^reserve-table/', reserv_table, name='reserv_table'),
]