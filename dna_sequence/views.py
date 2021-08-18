"""Sequence views"""
import json
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
from dna_seq_viewer.core.services.processing import parse_fasta
from dna_seq_viewer.core.services.authentication import current_user
from .models import GenBankSequence, FastaSequence

# from .models import DNASequence, ProteinSequence

# Create your views here.


class SequencesView(APIView):

    """Sequence views"""

    permission_classes = (IsAuthenticated,)

    @csrf_exempt
    def get(self, request):
        """Retrieve all sequences for current user"""
        user = current_user(request)
        sequences = list(GenBankSequence.objects.filter(user=user).values(
        )) + list(FastaSequence.objects.filter(user=user).values())
        return JsonResponse({'data': sequences})

    def post(self, request):
        """Save new sequence with user_id = current_user.id to database"""
        user = current_user(request)
        form_data = json.loads(request.body)
        sequence_dict = form_data['sequence']
        sequence_dict['user'] = user
        fasta_header, fasta_seq = parse_fasta(sequence_dict['raw_sequence'])
        sequence_dict['fasta_header'], sequence_dict['raw_sequence'] = fasta_header, fasta_seq
        if form_data['sequence_type'] == '0':
            GenBankSequence.objects.create(**sequence_dict)
        else:
            FastaSequence.objects.create(**sequence_dict)

        return HttpResponseRedirect('http://localhost:3000/sequences')


class SequenceView(APIView):
    """Sequence show view"""
    permission_classes = (IsAuthenticated,)

    @csrf_exempt
    def get(self, request, sequence_id):
        """Retrieve sequence by sequence id if belongs to signed-in user"""
        user = current_user(request)
        sequence = list(GenBankSequence.objects.filter(
            pk=sequence_id).values())[0]
        if sequence.user is user:
            return JsonResponse({'data': sequence})
        return JsonResponse({'data': None})
