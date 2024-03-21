from django.contrib import admin
from django.urls import path

from agendapersonal import views

app_name = 'agendapersonal'
urlpatterns = [
    path('', views.Index.as_view(), name = 'index'),
    path('<int:pk>/', views.VistaDetalles.as_view(), name ='detalles')
]