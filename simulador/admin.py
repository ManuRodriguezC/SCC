from django.contrib import admin
from .models import DeudaAporte, Extracupo

@admin.register(DeudaAporte)
class DeudaAporteAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Extracupo)
class ExtraCupoAdmin(admin.ModelAdmin):
    list_display = ['name']