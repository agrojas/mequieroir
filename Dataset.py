from Proposal import Proposal
from User import User

class Dataset:
	'Optional class documentation string'
	goodProposalFloor = 0.8
	goodProposalsQuantity = 3
	#users = []
	#proposals = []
	
	def initialize(self):
		self.users = User.getRandomUsers(10)
		self.proposals = Proposal.getRandomProposals(5000)
		#Dataset.users = self.user.getRandomUsers(10)
		#Dataset.proposals = self.proposal.getRandomProposals(200)
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
			if (proposal.skills[skillLabel] == 1):
				skillsToKnown += 1
				if (user.skills[skillLabel] == 1):
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
		for skillLabel in proposal.skills:
			headerLine += skillLabel + ","
		for benefitLabel in proposal.benefits:
			headerLine += benefitLabel + ","
		headerLine += "proposalId"
		return headerLine

	def getProposalAsLine(self,proposal):
		line = ""
		for skillLabel in proposal.skills:
			line += str(proposal.skills[skillLabel]) + ","
		for benefitLabel in proposal.benefits:
			line += str(proposal.benefits[benefitLabel]) + ","
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


