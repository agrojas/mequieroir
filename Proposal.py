import random

class Proposal:
	'Optional class documentation string'
	proposalCount = 0
	skillsDictionary = ["c","c++","c#","java","php","angular","cobol","objetos","ingles","git","viajar","equipo"]
	benefitsDictionary = ["flexibilidadHoraria","homeOffice","bonoObjetivo","capacitacion"]
	def __init__(self):
		Proposal.proposalCount += 1
		self.id = Proposal.proposalCount
		self.name = 'name' + str(self.id)
		self.phone = 'phone' + str(self.id)
		self.skills = {}
		for skillLabel in Proposal.skillsDictionary:
			self.skills[skillLabel] = 0
		self.benefits = {}
		for benefitLabel in Proposal.benefitsDictionary:
			self.benefits[benefitLabel] = 0
	
	def setRandomSkills(self):
		for key in self.skills:
			print(key)
			if (key != "objetos"):
				self.skills[key] = random.randint(0, 1)

			if (key == "c++" or key == "c#" or key == "java" and self.skills[key] == 1):
				self.skills["objetos"] = 1

	def setRandomBenefits(self):
		for key in self.benefits:
			if (key != "objetos"):
				self.benefits[key] = random.randint(0, 1)
			if (key == "c++" or key == "c#" or key == "java" and self.benefits[key] == 1):
				self.benefits[key] = 1

	def getRandomProposals(self,quantity):
		proposals = []
		for x in range(0, quantity):
			proposal = Proposal()
			proposal.setRandomSkills()
			proposal.setRandomBenefits()
			proposals.append(proposal)
		return proposals
