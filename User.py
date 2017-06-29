import random
from Dictionary import Dictionary

class User:
	'Optional class documentation string'
	userCount = 0

	def __init__(self):
		User.userCount += 1
		self.id = User.userCount
		self.name = 'name' + str(self.id)
		self.phone = 'phone' + str(self.id)
		self.skills = []
		self.goodProposals = []
		self.badProposal = []
		self.badCompanyProposal = []
		self.badConditionsProposal = []
		self.badSkillsProposal = []
	
	def setRandomSkills(self):
		self.skills = []
		while (len(self.skills)==0):
			for key in Dictionary.getSkills():
				if(random.randint(0, 1) == 1):
					self.skills.append(key)
					if (key == "c++" or key == "c#" or key == "java"):
						self.skills.append("objetos")

	@staticmethod			
	def getRandomUsers(quantity):
		users = []
		for x in range(0, quantity):
			user = User()
			user.setRandomSkills()
			users.append(user)
		return users



