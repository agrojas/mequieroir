import random
from Dictionary import Dictionary

class Proposal:
	'Optional class documentation string'
	proposalCount = 0
	
	def __init__(self):
		Proposal.proposalCount += 1
		self.id = Proposal.proposalCount
		self.name = 'name' + str(self.id)
		self.content = ""
		self.avatar = ""
		#self.phone = 'phone' + str(self.id)
		self.skills = []
		self.benefits = []
		self.expertise = ""
		self.area = []

	@staticmethod
	def getRandomProposals(quantity):
		proposals = []
		for x in range(0, quantity):
			proposal = Proposal()
			proposal.skills = Dictionary.getRandomSkills()
			proposal.expertise = Dictionary.getRandomExpertiseLevel()
			proposal.area = Dictionary.getAreas(proposal.skills)
			proposal.benefits = Dictionary.getRandomBenefits()
			proposals.append(proposal)
		return proposals
