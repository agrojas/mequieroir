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
	
	def setRandomSkills(self):
		self.skills = []
		while (len(self.skills)==0):
			for key in Dictionary.getSkills():
				if (key != "objetos"):
					if(random.randint(0, 1) == 1):
						self.skills.append(key)
						if (key == "c++" or key == "c#" or key == "java"):
							self.skills.append("objetos")

	def setRandomBenefits(self):
		self.benefits = []
		for key in Dictionary.getBenefits():
			if(random.randint(0, 1) == 1):
				self.benefits.append(key)

	@staticmethod
	def getRandomProposals(quantity):
		proposals = []
		for x in range(0, quantity):
			proposal = Proposal()
			proposal.setRandomSkills()
			proposal.setRandomBenefits()
			proposals.append(proposal)
		return proposals
