import pdb
import json
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.core.serializers import serialize
from django.core.exceptions import ValidationError
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
    form_data = json.loads(request.body)
    seq = DNASequence(**form_data)
    try:
        seq.full_clean()
        seq.save()
    except ValidationError as e:
        print(e)
    return HttpResponseRedirect('http://localhost:3000/sequences')
