from django import forms
from .models import DataSet, DataColumn


class DataSetForm(forms.ModelForm):
    columns = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = DataSet
        fields = ['name', 'description', 'json_file']


class DataColumnForm(forms.ModelForm):
    class Meta:
        model = DataColumn
        fields = ['name', 'data_type']