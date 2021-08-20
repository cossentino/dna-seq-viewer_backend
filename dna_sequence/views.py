"""Sequence views"""
import json
import sys
import pdb
from django.forms.models import model_to_dict
from operator import itemgetter
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from dna_seq_viewer.core.services.authentication import current_user
from dna_seq_viewer.core.services.biopython.parse import Parser
from registration.models import User
from .models import Sequence, GenBankAnnotationSet


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
        form_data = json.loads(request.body)
        input_file_format = form_data['input_file_format']
        parser = Parser(form_data['raw_sequence'], input_file_format)
        parser.parse()
        name, description, seq_type = itemgetter(
            'name', 'description', 'sequence_type')(form_data)
        for r in parser.records:
            del r.annotations['references']
            s = Sequence(seq=str(r.seq), name=name,
                         description=description, seq_type=seq_type, user=user)
            s.save()
            ga = GenBankAnnotationSet(**r.annotations, sequence=s)
            try:
                ga.save()
                return JsonResponse({'data': 'ok'})
            except:
                return JsonResponse({"Unexpected error": sys.exc_info()[0]})


class SequenceView(APIView):
    """Sequence show view"""
    permission_classes = (IsAuthenticated,)

    @ csrf_exempt
    def get(self, request, sequence_id):
        """Retrieve sequence by sequence id if belongs to signed-in user"""
        user = current_user(request)
        seq = Sequence.objects.get(pk=sequence_id)
        if user.id == seq.id:
            anns = seq.annotations.first()
            resp = JsonResponse(
                {'data': {'main': model_to_dict(seq), 'annotations': model_to_dict(anns)}})
            return resp
        return JsonResponse({'error': 'you aint authorized'})
