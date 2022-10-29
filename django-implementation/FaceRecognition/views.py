from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from FaceRecognition.models import *

# Create your views here.

def test(request):


    return render(request, 'index.html', {'name': 'Abdullah'})