# -*- coding: utf-8 -*-
from django.http import HttpResponse
from mock import *
import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('../../mequieroir')

# Now you can import your module
from Dataset import *

datasetInitializer = Dataset()

def index(request):
    return HttpResponse("Hello")

def initialize(request):
    datasetInitializer.initialize()
    datasetInitializer.saveProposalsToCsv("proposals.csv");
    response = "OK"
    return HttpResponse(response)


def detail(request, id):
    response = getData()
    return HttpResponse(response)

def results(request, id):
    response = "You're looking at the results of  %s."
    return HttpResponse(response % id)