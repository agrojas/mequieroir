# -*- coding: utf-8 -*-
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

import sys,traceback,json
# Add the ptdraft folder path to the sys.path list
print sys.path
sys.path.append('../../mequieroir')
#sys.path.append('..\\..\\aplicacionesInfo')

# Now you can import your module
from Dataset import *
from NeighborsTool import *

datasetInitializer = Dataset()
#datasetInitializer.randomInitialize()
datasetInitializer.fixedInitialize()
datasetInitializer.saveProposalsToCsv("proposals.csv");
neighborsTool = None
neighborsTool = NeighborsTool("proposals.csv")



def addProposal(request, id, proposalId):
    return HttpResponse("addProposal")

def jsonify(data):
    json_data = dict()
    for key, value in data.iteritems():
        if isinstance(value, list): # for lists
            value = [ jsonify(item) if isinstance(item, dict) else item for item in value ]
        if isinstance(value, dict): # for nested lists
            value = jsonify(value)
        if isinstance(key, int): # if key is integer: > to string
            key = str(key)
        if type(value).__module__=='numpy': # if value is numpy.*: > to python list
            value = value.tolist()
        if isinstance(value, User): # for User
            value = {"id":value.id,"name":value.name,"skills":value.skills,"expertise":value.expertise,"area":value.area}
        if isinstance(value, Proposal): # for User
            value = {"id":value.id,"benefits":value.benefits,"skills":value.skills,"content":value.content,"name":value.name,"area":value.area,"expertise":value.expertise}
        json_data[key] = value
    return json_data

def index(request):
    return HttpResponse("Hello")

def detail(request, id):
    response = getData()
    return HttpResponse(response)


def getProposalById(id):
    for proposal in datasetInitializer.getProposals():
        if (proposal.id == id):
            return proposal
    return {}

def makeCompleteResponse(data):
    response = {}
    proposals = []
    for x in range(0, len(data["proposal_id"])):    
        proposal = {}
        proposal["proposal"] = getProposalById(data["proposal_id"][x])
        proposal["distance"] = data["distance"][x]
        proposal["rank"] = data["rank"][x]
        proposals.append(proposal)

    response["proposals"] = proposals
    response["user"] = data["user"]
    response["goodProposal"] = data["goodProposal"]
    return response

def results(request, id):
    proposalToResponse = -1

    response = {}
    for user in datasetInitializer.users:
        if (user.id == int(id)):
            if(len(user.goodProposals) == 0):
                print 'el user no tiene ninguna buena propuesta para usar de referencia'
            for proposal in user.goodProposals:
                print 'encontro una buena propuesta en el user'
                proposalToResponse = proposal.id
                auxResponse = neighborsTool.query(proposal.id,5)
                if not ("proposal_id" in response):
                    response = auxResponse
                    response["user"] = user
                    response["goodProposal"] = proposal
                    break
                else:
                    if (("proposal_id" in response) and ("proposal_id" in auxResponse)):
                        response["proposal_id"] += auxResponse["proposal_id"]
                        response["rank"] += auxResponse["rank"]
                        response["distance"] += auxResponse["distance"]

    if (proposalToResponse == -1):   
        response = "ERROR"

    completeResponse = makeCompleteResponse(response)
    response_data = {}
    try:
        response_data['result'] = 'Success'
        response_data['data'] = jsonify(completeResponse)
    except:
        traceback.print_exc()
        response_data['result'] = 'Ouch!'
        response_data['data'] = 'Script has not ran correctly'
    
    return HttpResponse(JsonResponse(response_data), content_type="application/json")

