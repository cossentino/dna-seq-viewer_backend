import pdb
from django.urls import path
from .views import SequencesView, SequenceView, current_datetime


APP_NAME = 'dna_sequence'

urlpatterns = [
    path('sequences', SequencesView.as_view(), name="sequences"),
    path('sequences/<int:sequence_id>',
         SequenceView.as_view(), name="sequence"),
    path('', current_datetime, name="datetime")
]
