import pdb
import json
from rest_framework.decorators import api_view, renderer_classes
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegistrationSerializer

# Create your views here.


@api_view(('POST',))
def login_view(request):
    form_data = json.loads(request.body)
    username = User.objects.get(email=form_data['email'].lower()).username
    user = authenticate(
        request, username=username, password=form_data['password'])
    if user:
        login(request, user)
        resp = JsonResponse({'data': model_to_dict(user)})
        return resp
    else:
        return JsonResponse({'data': 'error logging in'})


class RegistrationAPIView(APIView):
    # Allow any user (authenticated or not) to hit this endpoint.
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # The create serializer, validate serializer, save serializer pattern
        # below is common and you will see it a lot throughout this course and
        # your own work later on. Get familiar with it.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
