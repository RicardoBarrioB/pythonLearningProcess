from django import forms
from .models import DataSet

class DataSetForm(forms.ModelForm):
    class Meta:
        model = DataSet
        fields = ['name', 'description', 'file']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            # Esto es opcional para darle estilo al campo de descripción
        }