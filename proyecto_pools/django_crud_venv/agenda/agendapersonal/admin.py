from django.contrib import admin
from .models import Entrada, Actualizacion

class ActualizacionInLine(admin.StackedInline):
    model = Actualizacion


class EntradaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['titulo']}),
        (None,               {'fields': ['texto']}),
        ('Date information', {'fields': ['fecha_creacion'], 'classes': ['collapse']}),
    ]
    inlines = [ActualizacionInLine]
    list_display = ('titulo', 'fecha_creacion')

admin.site.register(Entrada, EntradaAdmin)
