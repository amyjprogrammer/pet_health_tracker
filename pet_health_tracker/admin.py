from django.contrib import admin

from .models import PetInfo, HealthTracker

admin.site.register(PetInfo)
admin.site.register(HealthTracker)
