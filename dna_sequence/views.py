import pdb
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse
from .serializers import DNASequenceSerializer
from .models import DNASequence

# Create your views here.


def dna_sequence(request):
    sequence = DNASequence.objects[0]
    serializer = DNASequenceSerializer(sequence)
    return JsonResponse(serializer)


@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def test_dna_sequence(request):
    sequence = DNASequence.objects.get(pk=2)
    serializer = DNASequenceSerializer(sequence)
    return Response(serializer.data)
