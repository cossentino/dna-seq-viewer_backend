from django.urls import path
from .views import save, test_dna_sequence


app_name = 'dna_sequence'

urlpatterns = [
    path('test', test_dna_sequence, name="test"),
    path('sequences/new', save, name="new")
]
