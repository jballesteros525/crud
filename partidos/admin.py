from django.contrib import admin
from .models import Partidos

class PartidosAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)

# Register your models here.
admin.site.register(Partidos, PartidosAdmin)