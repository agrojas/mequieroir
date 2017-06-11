class User:
	'Optional class documentation string'
	userCount = 0
	skillsDictionary = ["c","c++","c#","java","php","angular","cobol","objetos","ingles","git","viajar"]
	def __init__(self):
		User.userCount += 1
		self.id = User.userCount
		self.name = 'name' + self.id
		self.phone = 'phone' + self.id
		self.skills = {}
		for skillLabel in skillsDictionary:
			self.skills[skillLabel] = 0
		self.goodProposal = []
		self.badProposal = []
		self.badCompanyProposal = []
		self.badConditionsProposal = []
		self.badSkillsProposal = []
	
	def setRandomSkills(self):
		for key in self.skills:
			if (key != "objetos"):
				self.skills[key] = random.uniform(0, 1)
			if (key == "c++" or key == "c#" or key == "java" and self.skills[key] == 1):
				self.skills[key] = 1

	def getRandomUsers(self,quantity):
		users = []
		for x in range(0, quantity):
			user = User()
			user.setRandomSkills()
			users[x] = user
		return users



