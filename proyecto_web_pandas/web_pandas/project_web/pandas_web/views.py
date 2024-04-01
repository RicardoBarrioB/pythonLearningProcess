from django.shortcuts import render, redirect
from django.views.generic import *
from django.urls import reverse_lazy
import pandas as pd
from .models import DataSet, DataColumn
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from .forms import DataSetForm, DataColumnForm
import json
from django.http import JsonResponse, HttpResponseBadRequest


class DataSetListView(ListView):
    model = DataSet
    template_name = 'pandas_web/datasets.html'
    context_object_name = 'datasets'

    def get_queryset(self):
        return DataSet.objects.all()


class DataSetCreateView(LoginRequiredMixin, CreateView):
    model = DataSet
    template_name = 'pandas_web/dataset_form.html'
    form_class = DataSetForm
    success_url = reverse_lazy('data_sets')

    def post(self, request, *args, **kwargs):
        if 'json_file' in request.FILES:
            file = request.FILES['json_file']
            try:
                data = json.load(file)
                key = next(iter(data.values()), [])
                columns_choices = list(key[0].keys())
                return JsonResponse({'columns_choices': columns_choices})

            except json.JSONDecodeError:
                return HttpResponseBadRequest("El archivo no es un JSON válido.")
        else:
            return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['data_column_forms'] = [DataColumnForm(prefix=str(x)) for x in range(5)]
        else:
            context['data_column_forms'] = [DataColumnForm(prefix=str(x)) for x in range(5)]
        return context


"""
    def form_valid(self, form):
        with transaction.atomic():
            form.instance.uploaded_by = self.request.user
            self.object = form.save()
            data_column_forms = [DataColumnForm(self.request.POST, prefix=str(x)) for x in range(5)]
            if all([data_column_form.is_valid() for data_column_form in data_column_forms]):
                for data_column_form in data_column_forms:
                    data_column = data_column_form.save(commit=False)
                    data_column.data_set = self.object
                    data_column.save()
            else:
                return self.form_invalid(form)
        return super().form_valid(form)
"""


class DataSetDetailView(DetailView):
    model = DataSet
    template_name = 'pandas_web/dataset_detail.html'
    context_object_name = 'dataset'

    def get(self, request, pk):
        dataset = get_object_or_404(DataSet, pk=pk)
        return render(request, 'pandas_web/dataset_detail.html', {'dataset': dataset})


class DataSetUpdateView(UpdateView):
    model = DataSet
    template_name = 'pandas_web/dataset_form.html'
    form_class = DataSetForm

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)


class DataSetDeleteView(DeleteView):
    model = DataSet
    success_url = reverse_lazy('data_sets')
    template_name = 'pandas_web/dataset_confirm_delete.html'

    def post(self, request, pk):
        dataset = get_object_or_404(DataSet, pk=pk)
        dataset.delete()
        return redirect('data_sets')
