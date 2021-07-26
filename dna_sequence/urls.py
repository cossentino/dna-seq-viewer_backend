from django.urls import path
from .views import test_dna_sequence


app_name = 'dna_sequence'

urlpatterns = [
    path('test', test_dna_sequence, name="test"),
]
