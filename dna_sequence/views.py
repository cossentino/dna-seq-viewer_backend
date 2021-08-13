import pdb
import json
import io
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.http import JsonResponse, HttpResponseRedirect
from dna_seq_viewer.core.services.processing import parse_fasta
from dna_seq_viewer.core.services.authentication import current_user

from .models import DNASequence, ProteinSequence

# Create your views here.


class SequencesView(APIView):
    permission_classes = (IsAuthenticated,)

    @csrf_exempt
    def get(self, request):
        user = current_user(request)
        sequences = list(ProteinSequence.sequences.filter(user=user).values())
        return JsonResponse({'data': sequences})

    def post(self, request):
        user = current_user(request)
        form_data = json.loads(request.body)
        sequence_dict = form_data['sequence']
        sequence_dict['user'] = user
        fasta_header, fasta_seq = parse_fasta(sequence_dict['raw_sequence'])
        sequence_dict['fasta_header'], sequence_dict['raw_sequence'] = fasta_header, fasta_seq
        if form_data['sequence_type'] == '0':
            seq = DNASequence.sequences.create(**sequence_dict)
        else:
            seq = ProteinSequence.sequences.create(**sequence_dict)

        return HttpResponseRedirect('http://localhost:3000/sequences')


class SequenceView(APIView):
    permission_classes = (IsAuthenticated,)

    @csrf_exempt
    def get(self, request, sequence_id):
        user = current_user(request)
        sequence = list(ProteinSequence.sequences.filter(
            pk=sequence_id).values())[0]
        return JsonResponse({'data': sequence})
