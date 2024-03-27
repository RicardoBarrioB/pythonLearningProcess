from django.contrib import admin
from django.urls import path
from .views import DataSetListView

urlpatterns = [
    path('data_sets/', DataSetListView.as_view(), name='data_sets'),
]