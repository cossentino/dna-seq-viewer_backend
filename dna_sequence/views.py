import pdb
import json
import io
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.http import JsonResponse, HttpResponseRedirect
from dna_seq_viewer.core.services.processing import parse_fasta
from dna_seq_viewer.core.services.authentication import current_user

from .models import DNASequence

# Create your views here.


class SequencesView(APIView):
    permission_classes = (IsAuthenticated,)

    @csrf_exempt
    def get(self, request):
        user = current_user(request)
        sequences = list(DNASequence.sequences.filter(user=user).values())
        return JsonResponse({'data': sequences})

    def post(self, request):
        user = current_user(request)
        form_data = json.loads(request.body)
        del form_data['sequence_type']
        form_data['user'] = user
        fasta_header, fasta_seq = parse_fasta(form_data['raw_sequence'])
        form_data['fasta_header'], form_data['raw_sequence'] = fasta_header, fasta_seq
        seq = DNASequence.sequences.create(**form_data)
        return HttpResponseRedirect('http://localhost:3000/sequences')


class SequenceView(APIView):
    permission_classes = (IsAuthenticated,)

    @csrf_exempt
    def get(self, request, sequence_id):
        user = current_user(request)
        sequence = list(DNASequence.sequences.filter(
            pk=sequence_id).values())[0]
        return JsonResponse({'data': sequence})
