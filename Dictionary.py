import random
class Dictionary(object):
	#skills = ["c","c++","c#","java","php","angular","cobol","objetos","ingles","git","viajar","equipo","UML","analisis"]
	skills = ["c","c++","c#","java","php","angular","cobol","objetos","ingles","git","viajar","equipo","UML","Front End","Back End","MySql","MsSql","Deployer","Oracle","Linux","analisis"]
	expertiseLevels = ["Junior","Semi-Senior","Senior"]
	areas = ["Developer","DBA","QA","Analista Funcional","Embebidos"]
	benefits = ["Flexibilidad Horaria","Home Office","Bono Objetivo","capacitacion","Descuentos corporativos","OSDE","MEDICUS"]
	@classmethod
	def getSkills(self):
		return self.skills

	@classmethod
	def getBenefits(self):
		return self.benefits

	@classmethod
	def getExpertiseLevels(self):
		return self.expertiseLevels

	@classmethod
	def getRandomExpertiseLevel(self):
		result = self.expertiseLevels[random.randint(0,2)]
		return result

	@classmethod
	def getAllAreas(self):
		return self.areas

	@classmethod
	def getAreas(self,skills):
		result = []
		if(("MySql" in skills) or ("MsSql" in skills) or ("Oracle" in skills)):
			result.append("DBA")
		if(("c++" in skills) or ("c#" in skills) or ("java" in skills) or ("cobol" in skills)):
			result.append("Developer")
		if(("analisis" in skills) or ("UML" in skills)):
			result.append("Analista Funcional")
		return result

	@classmethod
	def getRandomBenefits(self):
		result = []
		for key in self.benefits:
			if(random.randint(0, 1) == 1):
				result.append(key)
		return result

	@classmethod
	def getRandomSkills(self):
		result = []
		while (len(result)==0):
			for key in self.skills:
				if (key != "objetos"):
					if(random.randint(0, 1) == 1):
						result.append(key)
						if (key == "c++" or key == "c#" or key == "java"):
							result.append("objetos")
		return result