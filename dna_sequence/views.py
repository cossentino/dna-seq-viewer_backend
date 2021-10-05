"""Sequence views"""
import json
from .models import GenBankAnnotationSet, Sequence

import pdb


from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from dna_seq_viewer.core.services.authentication import current_user
from dna_seq_viewer.core.services.biopython.parse import Parser
from dna_seq_viewer.core.services.protein_analysis import aa_breakdown
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .helpers import create_feature

import datetime

# Create your views here.

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


class SequencesView(APIView):
    """Sequence views"""
    permission_classes = (IsAuthenticated,)

    @csrf_exempt
    def get(self, request):
        """Retrieve all sequences for current user"""
        user = current_user(request)
        sequences = list(Sequence.objects.filter(user=user).values())
        return JsonResponse({'data': sequences})

    def post(self, request):
        """Save new sequence with user_id = current_user.id to database"""
        user = current_user(request)
        data = json.loads(request.body)
        filetype = data['input_file_format']
        parser = Parser(data['raw_sequence'], filetype)
        for rec in parser.records:
            seq = Sequence(seq=str(rec.seq),
                           name=data['name'],
                           description=data['description'],
                           seq_type=data['sequence_type'],
                           user=user)
            seq.save()
            if seq.id:
                annotations = GenBankAnnotationSet.new(
                    **rec.annotations, sequence=seq)
                annotations.save()
                for feature in rec.features:
                    create_feature(feature, seq)

            return JsonResponse({'data': 'ok'})


class SequenceView(APIView):
    """Sequence show view"""
    permission_classes = (IsAuthenticated,)

    @csrf_exempt
    def get(self, request, sequence_id):
        """Retrieve sequence by sequence id if belongs to signed-in user"""
        user = current_user(request)
        seq = Sequence.objects.get(pk=sequence_id)
        if user.id == seq.user.id:
            if request.GET.get('analysis'):
                return JsonResponse({'data': aa_breakdown(seq.seq)})
            resp = JsonResponse(
                {'data':
                    {'main': model_to_dict(seq),
                     'annotations': model_to_dict(seq.annotations.first()),
                     'features': {i: model_to_dict(f) for i, f in enumerate(seq.features.all())}}
                 })
            return resp
        return JsonResponse({'error': 'you aint authorized'})
