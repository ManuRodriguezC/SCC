from django import forms
from .models import Extracupo, DeudaAporte, Salary

    
class ExtracupoForm(forms.ModelForm):
    """"""
    class Meta:
        model = Extracupo
        fields = ['name', 'tasa', 'montoMax', 'plazoMin', 'plazoMax', 'garantia', 'requisitos']
        labels = {
            'name': 'Nombre',
            'tasa': 'Tasa del credito',
            'montoMax': 'Monto maximo',
            'plazoMin': 'Plazo minimo',
            'plazoMax': 'Plazo maximo',
            'garantia': 'Garantias del credito',
            'requisitos': 'Requisitos del credito'
        }

class DeudaAporteForm(forms.ModelForm):
    """"""
    class Meta:
        model = DeudaAporte
        fields = ['name', 'tasa', 'montoMax', 'plazoMin', 'plazoMax', 'garantia', 'requisitos']
        labels = {
            'name': 'Nombre',
            'tasa': 'Tasa del credito',
            'montoMax': 'Monto maximo',
            'plazoMin': 'Plazo minimo',
            'plazoMax': 'Plazo maximo',
            'garantia': 'Garantias del credito',
            'requisitos': 'Requisitos del credito'
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