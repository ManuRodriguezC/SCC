from django.contrib import admin
from .models import DeudaAporte, Extracupo, SocialesRetencion, Sociales, Extra, Salary, Tasas

# @admin.register(DeudaAporte)
# class DeudaAporteAdmin(admin.ModelAdmin):
#     list_display = ['name']


# @admin.register(Extracupo)
# class ExtraCupoAdmin(admin.ModelAdmin):
#     list_display = ['name']
    
@admin.register(SocialesRetencion)
class SocialesRetencionAdmin(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(Sociales)
class SocialesAdmin(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(Extra)
class ExtraAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Salary)
class ExtraAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']

@admin.register(Tasas)
class TasasAdmin(admin.ModelAdmin):
    list_display = ['name', 'tasa']