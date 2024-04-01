from django import forms
from .models import DataSet, DataColumn


class DataSetForm(forms.ModelForm):
    columns = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = DataSet
        fields = ['name', 'description', 'file']

    def __init__(self, *args, **kwargs):
        columns_choices = kwargs.pop('columns_choices', [])
        super().__init__(*args, **kwargs)
        self.fields['columns'].choices = [(col, col) for col in columns_choices]
        print(columns_choices)


class DataColumnForm(forms.ModelForm):
    class Meta:
        model = DataColumn
        fields = ['name', 'data_type']