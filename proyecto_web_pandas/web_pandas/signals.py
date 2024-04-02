'''from django.db.models.signals import post_save
from django.dispatch import receiver
import pandas as pd

from .models import DataSet, DataColumn, DataPoint

@receiver(post_save, sender=DataSet)
def generate_data_columns_and_points(sender, instance, created, **kwargs):
    if created:  # Solo si se crea un nuevo DataSet
        # Lee el archivo JSON asociado al DataSet
        json_file_path = instance.json_file.path
        df = pd.read_json(json_file_path)

        # Crea DataColumns basados en las columnas del DataFrame
        for column_name, data_type in zip(df.columns, df.dtypes):
            data_column = DataColumn.objects.create(
                name=column_name,
                data_type=str(data_type),
                data_set=instance
            )

        # Crea DataPoints para cada fila en el DataFrame
        for index, row in df.iterrows():
            for column_name, value in row.items():
                data_column = DataColumn.objects.get(name=column_name, data_set=instance)
                DataPoint.objects.create(column=data_column, value=value)'''