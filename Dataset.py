from Proposal import Proposal
from User import User
from FixedInitializer import FixedInitializer
from Dictionary import Dictionary

class Dataset:
	'Optional class documentation string'
	goodProposalFloor = 1
	goodProposalsQuantity = 3
	
	def __init__(self):
		self.users = []
		self.proposals = []

	def fixedInitialize(self):
		FixedInitializer.initialize(self.users,self.proposals)
		self.setUsersGoodProposals()

	def randomInitialize(self):
		self.users = User.getRandomUsers(10)
		self.proposals = Proposal.getRandomProposals(5000)
		self.setUsersGoodProposals()

	def getProposals(self):
		return self.proposals

	def setUsersGoodProposals(self):
		for user in self.users:
			selectedProposalRank = 0
			selectedProposal = None
			for proposal in self.proposals:
				currentProposalRank = self.howGoodProposalIs(user,proposal)
				if (currentProposalRank > selectedProposalRank):
					selectedProposal = proposal
					selectedProposalRank = currentProposalRank
				if (selectedProposalRank > Dataset.goodProposalFloor):
					break	
			user.goodProposals.append(selectedProposal)	

	#def isGoodProposal(self,user,proposal):
	#	skillsToKnown = 0
	#	skillsKnown = 0
	#	for skillLabel in proposal.skills:
	#		skillsToKnown += 1
	#		if (skillLabel in user.skills):
	#			skillsKnown +=1
	#	if (skillsKnown/float(skillsToKnown)>=Dataset.goodProposalFloor):
	#		#print 'skillsKnown ' + str(skillsKnown) + 'skillsToKnown ' + str(skillsToKnown) + 'hegith ' + str(skillsKnown/float(skillsToKnown))
	#		return True
	#	return False

	def howGoodProposalIs(self,user,proposal):
		wanted = 0
		matched = 0
		for skillLabel in proposal.skills:
			wanted += 1
			if (skillLabel in user.skills):
				matched +=1
		for areaLabel in proposal.area:
			wanted += 1
			if (areaLabel in user.area):
				matched +=1
		if (proposal.expertise != ""):		
			wanted += 1
			if (proposal.expertise == user.expertise):
				matched +=1
		return matched/float(wanted) 

	def getProposalHeaderLine(self,proposal):
		headerLine = ""
		for skillLabel in Dictionary.getSkills():
			headerLine += skillLabel + ","
		for expertiseLevelLabel in Dictionary.getExpertiseLevels():
			headerLine += expertiseLevelLabel + ","
		for areaLabel in Dictionary.getAllAreas():
			headerLine += areaLabel + ","	
		for benefitLabel in Dictionary.getBenefits():
			headerLine += benefitLabel + ","
		headerLine += "proposalId"
		return headerLine

	def getProposalAsLine(self,proposal):
		line = ""
		for skillLabel in Dictionary.getSkills():
			skillValue = 0
			if(skillLabel in proposal.skills):
				skillValue = 1
			line += str(skillValue) + ","
		for expertiseLevel in Dictionary.getExpertiseLevels():
			expertiseValue = 0
			if (expertiseLevel == proposal.expertise):
				expertiseValue = 1
			line += str(expertiseValue) + ","
		for areaLabel in Dictionary.getAllAreas():
			areaValue = 0
			if (areaLabel in proposal.area):
				areaValue = 1
			line += str(areaValue) + ","
		for benefitLabel in Dictionary.getBenefits():
			benefitValue = 0
			if (benefitLabel in proposal.benefits):
				benefitValue = 1
			line += str(benefitValue) + ","
		line += str(proposal.id)
		return line

	def saveProposalsToCsv(self,datasetPath):
		file = open(datasetPath,"w")
		count = 0
		for proposal in self.proposals:
			if (count == 0):
				file.write(self.getProposalHeaderLine(proposal)+"\n")
			file.write(self.getProposalAsLine(proposal)+"\n")
			count+=1
		file.close


