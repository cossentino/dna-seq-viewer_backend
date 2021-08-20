"""Sequence views"""
import json
import pdb
from operator import itemgetter

from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dna_seq_viewer.core.services.authentication import current_user
from dna_seq_viewer.core.services.biopython.parse import Parser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import GenBankAnnotationSet, Sequence

# Create your views here.


class SequencesView(APIView):

    """Sequence views"""

    permission_classes = (IsAuthenticated,)

    @csrf_exempt
    def get(self, request):
        """Retrieve all sequences for current user"""
        user = current_user(request)
        sequences = list(Sequence.objects.filter(user=user).values(
        ))
        return JsonResponse({'data': sequences})

    def post(self, request):
        """Save new sequence with user_id = current_user.id to database"""
        user = current_user(request)
        data = json.loads(request.body)
        filetype = data['input_file_format']
        parser = Parser(data['raw_sequence'], filetype)
        name, description, seq_type = itemgetter(
            'name', 'description', 'sequence_type')(data)
        for rec in parser.records:
            seq = Sequence(seq=str(rec.seq), name=name,
                           description=description, seq_type=seq_type, user=user)
            annotations = GenBankAnnotationSet.new(
                **rec.annotations, sequence=seq)
            seq.save()
            annotations.save()
            return JsonResponse({'data': 'ok'})


class SequenceView(APIView):
    """Sequence show view"""
    permission_classes = (IsAuthenticated,)

    @ csrf_exempt
    def get(self, request, sequence_id):
        """Retrieve sequence by sequence id if belongs to signed-in user"""
        user = current_user(request)
        seq = Sequence.objects.get(pk=sequence_id)
        if user.id == seq.user.id:
            anns = seq.annotations.first()
            resp = JsonResponse(
                {'data': {'main': model_to_dict(seq), 'annotations': model_to_dict(anns)}})
            return resp
        return JsonResponse({'error': 'you aint authorized'})
