# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from mysite.models import Tables, Reservations

# Register your models here.

admin.site.register(Tables)
admin.site.register(Reservations)
