from Proposal import Proposal
from User import User
class Dataset:
	'Optional class documentation string'
	goodProposalFloor = 0.5
	goodProposalsQuantity = 3
	#users = []
	#proposals = []
	
	def initialize(self):
		self.users = User().getRandomUsers(10)
		self.proposals = Proposal().getRandomProposals(200)
		#Dataset.users = self.user.getRandomUsers(10)
		#Dataset.proposals = self.proposal.getRandomProposals(200)
		self.setUsersGoodProposals()

	def setUsersGoodProposals(self):
		for usersKey in self.users:
			for proposalKey in self.proposals:
				if (len(self.users[usersKey].goodProposals)<Dataset.goodProposalsQuantity):
					if(isGoodProposal(self.users[usersKey],self.proposals[proposalKey])):
						self.users[usersKey].goodProposals.append(self.proposals[proposalKey])
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
		if (skillsKnown/float(skillsToKnown)>Dataset.goodProposalFloor):
			return True
		return False

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
			headerLine += proposal.skills[skillLabel] + ","
		for benefitLabel in proposal.benefits:
			headerLine += proposal.benefits[benefitLabel] + ","
		headerLine += proposal.id
		return headerLine

	def saveProposalsToCsv(self,datasetPath):
		file = open(datasetPath,"w")
		for x in self.proposals:
			if (x == 0):
				file.write(getProposalHeaderLine(self.proposal))
			file.write(getProposalAsLine(self.proposal))
		file.close


