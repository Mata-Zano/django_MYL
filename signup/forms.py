from django import forms
from .models import compra

# primero : bd , segundo : se muestra
productos_choices = [
    ('masterDog','Master Dog'),
    ('pedigree','Pedigree'),
    ('purina','Purina'),
    ('Whiskas','Whiskas'),
]

class compraForm(forms.ModelForm):
    class Meta:
        model = compra
        fields = ['nombre_producto', 'cantidad','direccion','numero_telefono']
        widgets = {
            'nombre_producto' : forms.Select(choices=productos_choices, attrs={'class':'form-control'}),
            'cantidad' : forms.NumberInput(attrs={'class':'form-control'}),
            'direccion' : forms.TextInput(attrs={'class':'form-control'}),
            'numero_telefono' : forms.TextInput(attrs={'class':'form-control'}),
        }