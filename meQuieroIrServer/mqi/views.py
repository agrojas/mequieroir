# -*- coding: utf-8 -*-
from django.http import HttpResponse
from mock import *
import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('../../mequieroir')

# Now you can import your module
from Dataset import *
from NeighborsTool import *

datasetInitializer = Dataset()
neighborsTool = None
datasetInitializer.initialize()
datasetInitializer.saveProposalsToCsv("proposals.csv");
neighborsTool = NeighborsTool("proposals.csv")


def index(request):
    return HttpResponse("Hello")

def detail(request, id):
    response = getData()
    return HttpResponse(response)

def results(request, id):
    proposalToResponse = -1
    for proposal in datasetInitializer.proposals:
        if (str(proposal.id) == str(id)):
            proposalToResponse = id
            response = neighborsTool.query(int(id),5)
    neighborsTool.modelSumary()   
    


    if (proposalToResponse == -1):   
        response = "ERROR"


    return HttpResponse(response)