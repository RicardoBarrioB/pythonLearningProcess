from django.shortcuts import render
from .models import DataSet
from django.views.generic import *
from django.urls import reverse_lazy
import pandas as pd
from .models import DataSet, DataColumn
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from .forms import DataSetForm, DataColumnForm


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
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Leer el archivo CSV y obtener las columnas
        columns_choices = ['Columna1', 'Columna2', 'Columna3']  # Reemplaza esto con tu lógica para obtener las columnas
        kwargs['columns_choices'] = columns_choices
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['data_column_forms'] = [DataColumnForm(prefix=str(x)) for x in range(5)]
        else:
            context['data_column_forms'] = [DataColumnForm(prefix=str(x)) for x in range(5)]
        return context

    def form_valid(self, form):
        with transaction.atomic():
            form.instance.uploaded_by = self.request.user
            self.object = form.save()  # Guardar el DataSet primero
            data_column_forms = [DataColumnForm(self.request.POST, prefix=str(x)) for x in range(5)]
            if all([data_column_form.is_valid() for data_column_form in data_column_forms]):
                for data_column_form in data_column_forms:
                    data_column = data_column_form.save(commit=False)
                    data_column.data_set = self.object  # Asignar el DataSet creado
                    data_column.save()  # Guardar cada DataColumn asociado
            else:
                return self.form_invalid(form)
        return super().form_valid(form)

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
    form_class = DataSetForm  # Especifica el formulario a utilizar

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user  # Asigna el usuario actual como el que subió el conjunto de datos
        return super().form_valid(form)

class DataSetDeleteView(DeleteView):
    model = DataSet
    success_url = reverse_lazy('data_sets')
    template_name = 'pandas_web/dataset_confirm_delete.html'

    def post(self, request, pk):
        dataset = get_object_or_404(DataSet, pk=pk)
        dataset.delete()
        return redirect('data_sets')
