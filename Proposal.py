class Proposal:
	'Optional class documentation string'
	proposalCount = 0
	skillsDictionary = ["c","c++","c#","java","php","angular","cobol","objetos","ingles","git","viajar","equipo"]
	benefitDictionary = ["flexibilidadHoraria","homeOffice","bonoObjetivo","capacitacion"]
	def __init__(self):
		Proposal.proposalCount += 1
		self.id = proposal.proposalCount
		self.name = 'name' + self.id
		self.phone = 'phone' + self.id
		self.skills = {}
		for skillLabel in skillsDictionary:
			self.skills[skillLabel] = 0
		self.benefits = {}
		for benefitLabel in benefitsDictionary:
			self.benefits[benefitLabel] = 0
	
	def setRandomSkills(self):
		for key in self.skills:
			if (key != "objetos"):
				self.skills[key] = random.uniform(0, 1)
			if (key == "c++" or key == "c#" or key == "java" and self.skills[key] == 1):
				self.skills[key] = 1

	def setRandomBenefits(self):
		for key in self.benefits:
			if (key != "objetos"):
				self.benefits[key] = random.uniform(0, 1)
			if (key == "c++" or key == "c#" or key == "java" and self.benefits[key] == 1):
				self.benefits[key] = 1

	def getRandomProposals(self,quantity):
		proposals = []
		for x in range(0, quantity):
			proposal = proposal()
			proposal.setRandomSkills()
			proposal.setRandomBenefits()
			proposals[x] = proposal
		return proposals
