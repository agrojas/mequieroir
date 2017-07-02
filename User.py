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
		self.expertise = ""
		self.area = []
		self.goodProposals = []
		self.badProposal = []
		self.badCompanyProposal = []
		self.badConditionsProposal = []
		self.badSkillsProposal = []

	@staticmethod			
	def getRandomUsers(quantity):
		users = []
		for x in range(0, quantity):
			user = User()
			user.skills = Dictionary.getRandomSkills()
			user.expertise = Dictionary.getRandomExpertiseLevel()
			user.area = Dictionary.getAreas(user.skills)
			users.append(user)
		return users



