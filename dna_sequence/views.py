import pdb
import json
import io
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


def parse_fasta(fasta_string):
    """Takes in string representation of FASTA-formatted text file and returns 
    2-tuple of (header, sequence)"""
    buf = io.StringIO(fasta_string)
    header, current_line, sequence = buf.readline().rstrip(), buf.readline().rstrip(), ""
    while len(current_line) > 0:
        sequence = sequence + current_line
        current_line = buf.readline().rstrip()
    buf.close()
    return (header, sequence)


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
    fasta_header, fasta_seq = parse_fasta(form_data['raw_sequence'])
    form_data['fasta_header'], form_data['raw_sequence'] = fasta_header, fasta_seq
    seq = DNASequence.sequences.create(**form_data)
    return HttpResponseRedirect('http://localhost:3000/sequences')
