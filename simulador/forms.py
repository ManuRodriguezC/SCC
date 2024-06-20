from django import forms
from .models import Salary, SocialesRetencion, Sociales, Extra, Tasas

class SocialesRetencionForm(forms.ModelForm):
    """"""
    class Meta:
        model = SocialesRetencion
        fields = ['name', 'rango1', 'rango2', 'rango3', 'rango4', 'rango5', 'rango6', 'rango7', 'aportesMax', 'plazoMax', 'garantia', 'requisitos']
        labels = {
            'name': 'Nombre',
            'rango1': 'Tasa de 1 a 6 meses',
            'rango2': 'Tasa de 7 a 12 meses',
            'rango3': 'Tasa de 13 a 24 meses',
            'rango4': 'Tasa de 25 a 36 meses',
            'rango5': 'Tasa de 37 a 48 meses',
            'rango6': 'Tasa de 49 a 60 meses',
            'rango7': 'Tasa de 61 a 72 meses',
            'aportesMax': 'Porcentaje maximo a prestar',
            'plazoMax': 'Plazo maximo de cuotas',
            'garantia': 'Garantias del credito',
            'requisitos': 'Requisitos del credito'
        }
 
class SocialesForm(forms.ModelForm):
    """"""
    class Meta:
        model = Sociales
        fields = ['name', 'rango1', 'rango2', 'rango3', 'rango4', 'rango5', 'rango6', 'rango7', 'rango8', 'plazoMax', 'garantia', 'requisitos']
        labels = {
            'name': 'Nombre',
            'rango1': 'Tasa de 1 a 6 meses',
            'rango2': 'Tasa de 7 a 12 meses',
            'rango3': 'Tasa de 13 a 24 meses',
            'rango4': 'Tasa de 25 a 36 meses',
            'rango5': 'Tasa de 37 a 48 meses',
            'rango6': 'Tasa de 49 a 60 meses',
            'rango7': 'Tasa de 61 a 72 meses',
            'rango8': 'Tasa de 73 a 120 meses',
            'plazoMax': 'Plazo maximo de cuotas',
            'garantia': 'Garantias del credito',
            'requisitos': 'Requisitos del credito'
        }

class ExtraForm(forms.ModelForm):
    """"""
    class Meta:
        model = Extra
        fields = ['name', 'plazoMax', 'garantia', 'requisitos']
        labels = {
            'name': 'Nombre',
            'plazoMax': 'Plazo maximo de cuotas',
            'garantia': 'Garantias del credito',
            'requisitos': 'Requisitos del credito'
        }
        
class TasasForm(forms.ModelForm):
    """"""
    class Meta:
        model = Tasas
        fields = ['name', 'scoreMin', 'scoreMax', 'fianza', 'plazoMax', 'tasa']
        labels = {
            'name': 'Nombre',
            'scoreMin': 'Score minimo',
            'scoreMax': 'Score maximo',
            'fianza': 'Porcentaje fianza',
            'plazoMax': 'Plazo maximo de cuotas',
            'tasa': 'Tasa',
            }

class SalaryForm(forms.ModelForm):
    """"""
    value = forms.CharField(widget=forms.TextInput(attrs={'oninput': "handleChange('id_value')"}))
    class Meta:
        model = Salary
        fields = ['name', 'value']
        labels = {
            'name': 'Nombre',
            'value': 'Valor actual de SMMLV'
        }

# class ExtraForm(forms.ModelForm):
#     """"""
#     class Meta:
#         model = Extra
#         fields = ['name', 'scoreMin', 'scoreMax', 'fianza', 'plazoMax', 'garantia', 'tasa']
#         labels = {
#             'name': 'Nombre',
#             'plazoMax': 'Plazo maximo de cuotas',
#             'garantia': 'Garantias del credito',
#             'requisitos': 'Requisitos del credito'
#         }

# class ExtracupoForm(forms.ModelForm):
#     """"""
#     class Meta:
#         model = SocialesRetencion
#         fields = ['name', 'tasa', 'montoMax', 'plazoMin', 'plazoMax', 'garantia', 'requisitos']
#         labels = {
#             'name': 'Nombre',
#             'tasa': 'Tasa del credito',
#             'montoMax': 'Monto maximo',
#             'plazoMin': 'Plazo minimo',
#             'plazoMax': 'Plazo maximo',
#             'garantia': 'Garantias del credito',
#             'requisitos': 'Requisitos del credito'
#         }

# class DeudaAporteForm(forms.ModelForm):
#     """"""
#     class Meta:
#         model = DeudaAporte
#         fields = ['name', 'tasa', 'montoMax', 'plazoMin', 'plazoMax', 'garantia', 'requisitos']
#         labels = {
#             'name': 'Nombre',
#             'tasa': 'Tasa del credito',
#             'montoMax': 'Monto maximo',
#             'plazoMin': 'Plazo minimo',
#             'plazoMax': 'Plazo maximo',
#             'garantia': 'Garantias del credito',
#             'requisitos': 'Requisitos del credito'
#         }

