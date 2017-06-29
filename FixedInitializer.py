# coding=utf-8
from Proposal import Proposal
from User import User

class FixedInitializer:
	'Optional class documentation string'
	
	@staticmethod
	def initialize(self,users,proposals):
		user = User()
		user.name = "user 1"
		user.skills = ["java","objetos"]
		users.append(proposal)

		user = User()
		user.name = "user 2"
		user.skills = ["analisis","UML"]
		users.append(proposal)

		proposal = Proposal()
		proposal.name = "Desarrollador Jr"
		proposal.avatar = "svg-1"
		proposal.skills = ["objetos","equipo"]
		proposal.benefits = ["Flexibilidad Horaria","Home Office"]
		proposal.content = "Mail: people@zedplan.com -Estamos en la búsqueda de un programador Junior. La persona seleccionada deberá poseer disponibilidad para asistir a nuestras oficinas ubicadas en zona Av. Gaona y Av. Boyaca, Capital Federal. Tiempo completo o medio tiempo.En nuestra empresa nos dedicamos a desarrollar todo tipo de Aplicaciones Web 2.0 con las implementación de las últimas tecnologías disponibles en el mercado. Junto con toda nuestra creatividad y experiencia tratamos de lograr soluciones innovadoras que generen un verdadero impacto tanto en nuestros clientes como en los usuarios de los sistemas que desarrollamos. Nuestros clientes son variados desde pequeñas pymes a importantes empresas. Tecnologias que utilizarás y aprenderás: -HTML 5: JavaScript, jQuery, Bootstrap. -PHP 5:POO. Framework MVC. -Nginx: optimizacion para entornos de producción. -MySQL:5.6, Stores, Triggers, Fulltext. -Control de versiones con GIT. Entornos para desarrollo: -Linux. Mail: people@zedplan.com"
		proposals.append(proposal)
		
		proposal = Proposal()
		proposal.name = "Desarrollador Java Ssr"
		proposal.avatar = "svg-1"
		proposal.skills = ["java","objetos","ingles","git","viajar","equipo"]
		proposal.benefits = ["Flexibilidad Horaria","Home Office","Bono Objetivo"]
		proposal.content = """IT Company se encuentra en la búsqueda de un Desarrollador Java Ssr. para sumarse al equipo de una importante empresa de seguros. 
		        Tareas/Responsabilidades: 
		        ·         Desarrollo de requerimientos. 
		        ·   Atender los pedidos de los usuarios sobre las aplicaciones a cargo, darle solución o adecuación. 
		        ·         Posicionarse en el puesto tomando rápidamente el control de las aplicaciones. 
		        ·         Comprender las necesidades de los usuarios y del negocio. 
		        Requisitos del puesto: 
		        ·         Orientamos la búsqueda a estudiante o graduado de sistemas. 
		        ·         Contar con al menos 2 años de experiencia en posiciones similares."""
		proposals.append(proposal)

		proposal = Proposal()
		proposal.name = "Analista Funcional"
		proposal.avatar = "svg-2"
		proposal.skills = ["analisis","ingles","git","viajar","equipo"]
		proposal.benefits = ["Flexibilidad Horaria","Home Office","Bono Objetivo","Capacitacion en Idiomas"]
		proposal.content = """Tareas y funciones:Interpretar, analizar y documentar requerimientos de Areas Internas y clientes externos. 
		        -Interpretar, analizar documentación Técnica y funcional. 
		        -Participar en la elaboración de Propuestas de solución a los requerimientos recibidos. Principalmente orientadas a Desarrollo de Recaudaciones en
		        Aplicaciones integradas a la línea de caja de las Entidades y a través de canales electrónicos.
		        -Elaborar documentación para Areas Internas y Clientes Externos"""
		proposals.append(proposal)

		proposal = Proposal()
		proposal.name = "Ingeniero de Desarrollo"
		proposal.avatar = "svg-3"
		proposal.skills = ["c","c++","c#","java","php","angular","cobol","objetos","ingles","git","viajar","equipo"]
		proposal.benefits = ["Home Office","Bono Objetivo","Capacitacion en Idiomas"]
		proposal.content = """Ingeniero de Desarrollo 
		          Las responsabilidades del puesto serán:
		          Controlar la contratación de servicios tecnológicos de la compañía
		          Realizar el análisis, diseño, desarrollo e implementación de aplicaciones de la compañía
		          Controlar el óptimo desempeño de las aplicaciones del negocio
		          Evaluar viabilidad técnica y económica en la adquisición de herramientas
		          Participar en la planificación y desarrollo de los requisitos relacionados con la ejecución de los proyectos tecnológicos
		          Trabajar en conjunto con los contratistas de distintos servicios en la resolución de los problemas técnicos de los productos.
		          Realizar seguimiento a los indicadores de gestión, e implementar mejoras de ser necesario
		          Establecer mecanismos de control para tratar el producto o servicio no conforme"""
		proposals.append(proposal)

		proposal = Proposal()
		proposal.name = "Desarrollador Java Sr"
		proposal.avatar = "svg-4"
		proposal.skills = ["c++","c#","java","objetos","ingles","git","equipo"]
		proposal.benefits = ["Flexibilidad Horaria","Home Office","Bono Objetivo","capacitacion"]
		proposal.content = """En Wavent, empresa Líder de Clasificados Online , estamos en la búsqueda de Java Developers Sr . Perteneciendo al equipo de tecnología regional de Navent no solo vas a diseñar, programar y crear nuevas funcionalidades, si no que vas a participar de la totalidad del ciclo de desarrollo del producto.
		Este equipo es quien se encarga de colaborar con la mejora continua de la plataforma que da servicio a todos nuestros portales."""
		proposals.append(proposal)

		proposal = Proposal()
		proposal.name = "Programador .NET"
		proposal.avatar = "svg-2"
		proposal.skills = ["c#","objetos","ingles","git","viajar","equipo"]
		proposal.benefits = ["Flexibilidad Horaria","Bono Objetivo","capacitacion"]
		proposal.content = """IT Resources se encuentra en la búsqueda de un Programador .Net para sumarse al equipo de una importante cadena de mayoristas.
		        Tareas/Responsabilidades:
		        Desarrollo y Mantenimiento evolutivo .NET y de interfaces con periféricos (POSNET/Impresoras Fiscales).
		        Análisis de nuevos requerimientos
		        Documentación.
		        Requisitos excluyentes:
		        Orientamos la búsqueda a estudiantes en curso o graduados de Sistemas.
		        Contar con al menos 2 años de experiencia en posiciones similares.
		        Capacidad de análisis de procesos y diseño de soluciones."""
		proposals.append(proposal)

		proposal = Proposal()
		proposal.name = "Especialista en seguridad de la informacion y ciberseguridad"
		proposal.avatar = "svg-4"
		proposal.skills = ["c#","c","c++","ingles","git","viajar","equipo"]
		proposal.benefits = ["Flexibilidad Horaria","Home Office","Bono Objetivo","capacitacion"]
		proposal.content = """Objetivo de la posición
				Estamos buscando un investigador en temas relacionados con Seguridad de la Información y CiberSeguridad con ganas de proporcionar ideas nuevas y disruptivas en investigaciones y análisis sobre Seguridad de la información. Desarrollar nuevas herramientas, conceptos e informes. Mantener un profundo conocimiento sobre los diferentes ecosistemas de seguridad, nuevas tecnologías y tendencias."""
  