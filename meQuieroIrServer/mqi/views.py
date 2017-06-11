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
    response = {}
    for user in datasetInitializer.users:
        if (user.id == int(id)):
            for proposal in user.goodProposals:
                proposalToResponse = proposal.id
                auxResponse = neighborsTool.query(proposal.id,5)
                if not ("proposal_id" in response):
                    response = auxResponse
                else:
                    if (("proposal_id" in response) and ("proposal_id" in auxResponse)):
                        response["proposal_id"] += auxResponse["proposal_id"]
                        response["rank"] += auxResponse["rank"]
                        response["distance"] += auxResponse["distance"]
    #neighborsTool.modelSumary()   

    if (proposalToResponse == -1):   
        response = "ERROR"


    return HttpResponse(response)