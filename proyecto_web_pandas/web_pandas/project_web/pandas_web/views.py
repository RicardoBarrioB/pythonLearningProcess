from django.shortcuts import render
from .models import DataSet
from django.views.generic import ListView

class DataSetListView(ListView):
    model = DataSet
    template_name = 'pandas_web/datasets.html'
    context_object_name = 'datasets'

    def get_queryset(self):
        return DataSet.objects.all()


