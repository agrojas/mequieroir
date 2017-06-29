class Dictionary(object):
	skills = ["c","c++","c#","java","php","angular","cobol","objetos","ingles","git","viajar","equipo","UML","analisis","Front End","Back End","MySql","MsSql"]
	benefits = ["Flexibilidad Horaria","Home Office","Bono Objetivo","capacitacion"]
	@classmethod
	def getSkills(self):
		return self.skills

	@classmethod
	def getBenefits(self):
		return self.benefits