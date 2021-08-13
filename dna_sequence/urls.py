from django.urls import path
from .views import SequencesView, SequenceView


app_name = 'dna_sequence'

urlpatterns = [
    path('sequences', SequencesView.as_view(), name="sequences")
]
