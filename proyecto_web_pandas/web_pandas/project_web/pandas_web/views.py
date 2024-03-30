from django.shortcuts import render
from .models import DataSet
from django.views.generic import *
from django.urls import reverse_lazy
import pandas as pd
from .forms import DataSetForm
from .models import DataSet, DataColumn

class DataSetListView(ListView):
    model = DataSet
    template_name = 'pandas_web/datasets.html'
    context_object_name = 'datasets'

    def get_queryset(self):
        return DataSet.objects.all()

class DataSetCreateView(CreateView):
    model = DataSet
    template_name = 'pandas_web/dataset_form.html'
    form_class = DataSetForm
    success_url = reverse_lazy('data_sets')

    def form_valid(self, form):
        # Guarda el formulario y obtén la instancia de DataSet
        data_set = form.save(commit=False)
        data_set.uploaded_by = self.request.user

        # Procesa el archivo subido y crea instancias de DataColumn y DataPoint
        file = self.request.FILES['file']
        df = pd.read_csv(file)  # Lee el archivo CSV utilizando pandas
        columns = df.columns.tolist()  # Obtiene la lista de nombres de columnas del archivo

        # Crea instancias de DataColumn para cada columna en el archivo
        for column_name in columns:
            data_column = DataColumn.objects.create(name=column_name, data_set=data_set)
            # Crea instancias de DataPoint para cada valor en la columna
            for index, value in df[column_name].items():
                DataPoint.objects.create(column=data_column, value=value)

        # Guarda la instancia de DataSet y sus modelos relacionados
        data_set.save()

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
