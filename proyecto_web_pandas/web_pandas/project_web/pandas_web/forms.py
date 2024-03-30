from django import forms
from .models import DataSet, DataColumn

class DataSetForm(forms.ModelForm):
    columns = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = DataSet
        fields = ['name', 'description', 'file']

    def __init__(self, *args, **kwargs):
        # Recibe la lista de columnas del archivo CSV como un argumento adicional
        columns_choices = kwargs.pop('columns_choices', [])
        super().__init__(*args, **kwargs)
        # Establece las opciones del campo de selección múltiple
        self.fields['columns'].choices = [(col, col) for col in columns_choices]


class DataColumnForm(forms.ModelForm):
    class Meta:
        model = DataColumn
        fields = ['name', 'data_type']