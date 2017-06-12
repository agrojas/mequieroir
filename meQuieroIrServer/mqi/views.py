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
neighborsTool = None
datasetInitializer.initialize()
datasetInitializer.saveProposalsToCsv("proposals.csv");
neighborsTool = NeighborsTool("proposals.csv")


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

    response["proposals"] = proposals
    response["user"] = data["user"]
    return response

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
                    response["user"] = user
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
        response_data['message'] = json.dumps(jsonify(completeResponse))
    except:
        traceback.print_exc()
        response_data['result'] = 'Ouch!'
        response_data['message'] = 'Script has not ran correctly'
    
    return HttpResponse(JsonResponse(response_data), content_type="application/json")

