from Proposal import Proposal
from User import User
from FixedInitializer import FixedInitializer
from Dictionary import Dictionary

class Dataset:
	'Optional class documentation string'
	goodProposalFloor = 0.8
	goodProposalsQuantity = 3
	
	def __init__(self):
		self.users = []
		self.proposal = []

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
			for proposal in self.proposals:
				if (len(user.goodProposals) < Dataset.goodProposalsQuantity):
					if(self.isGoodProposal(user,proposal)):
						#print 'esta agregando una buena propuesta'
						user.goodProposals.append(proposal)
				else:
					break

	def isGoodProposal(self,user,proposal):
		skillsToKnown = 0
		skillsKnown = 0
		for skillLabel in proposal.skills:
			skillsToKnown += 1
			if (skillLabel in user.skills):
				skillsKnown +=1
		if (skillsKnown/float(skillsToKnown)>=Dataset.goodProposalFloor):
			#print 'skillsKnown ' + str(skillsKnown) + 'skillsToKnown ' + str(skillsToKnown) + 'hegith ' + str(skillsKnown/float(skillsToKnown))
			return True
		return False

	def howGoodProposalIs(self,user,proposal):
		skillsToKnown = 0
		skillsKnown = 0
		for skillLabel in proposal.skills:
			if (proposal.skills[skillLabel] == 1):
				skillsToKnown += 1
				if (user.skills[skillLabel] == 1):
					skillsKnown +=1
		return skillsKnown/float(skillsToKnown) 

	def getProposalHeaderLine(self,proposal):
		headerLine = ""
		for skillLabel in Dictionary.getSkills():
			headerLine += skillLabel + ","
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


