from django.db import models

class Entrada (models.Model):
    titulo = models.CharField(max_length=25)
    texto = models.CharField(max_length=300)
    fecha_creacion = models.DateTimeField('fecha_creacion')

    def __str__(self):
        return self.titulo


class Actualizacion (models.Model):
    tipo = models.CharField(max_length=10)
    fecha = models.DateField('fecha')
    hora = models.TimeField('hora')
    entrada = models.ForeignKey(Entrada, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo



