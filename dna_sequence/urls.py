from django.urls import path
from .views import save, index


app_name = 'dna_sequence'

urlpatterns = [
    path('sequences/new', save, name="new"),
    path('sequences', index, name="sequences")
]
