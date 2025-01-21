from django.contrib import admin

from django.contrib import admin
from .models import Cryptocurrency, SantimentData

admin.site.register(Cryptocurrency)
admin.site.register(SantimentData)