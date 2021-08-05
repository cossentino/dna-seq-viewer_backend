import pdb
import json
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import DNASequence

# Create your views here.


def dna_sequence(request):
    sequence = DNASequence.objects[0]


@api_view(('GET',))
@csrf_exempt
def index(request):
    sequences = list(DNASequence.sequences.values())
    return JsonResponse({'data': sequences})


@api_view(('POST',))
def save(request):
    attrs = json.loads(request.body)
    if attrs['sequence_type'] == '1':
        del attrs['sequence_type']
        sequence = DNASequence(**attrs)
    pdb.set_trace()
