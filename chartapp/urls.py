from django.urls import path
from .views import ChartJS

urlpatterns = [
    path('',ChartJS, name='chartjs')
]