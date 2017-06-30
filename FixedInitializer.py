# coding=utf-8
from Proposal import Proposal
from User import User

class FixedInitializer:
	'Optional class documentation string'
	
	@staticmethod
	def initialize(users,proposals):
		user = User()
		user.name = "java user"
		user.skills = ["java","objetos"]
		user.expertise = ["junior"]
		user.area = ["Developer"]
		users.append(user)

		user = User()
		user.name = "funcional user"
		user.skills = ["analisis","UML"]
		user.expertise = ["Senior"]
		user.area = ["Analista Funcional"]
		users.append(user)

		user = User()
		user.name = "DBA user"
		user.skills = ["MsSql","Deployer"]
		user.expertise = ["Semi-Senior"]
		user.area = ["DBA"]
		users.append(user)

		user = User()
		user.name = "Embebidos user"
		user.skills = ["c","c++"]
		user.expertise = ["Semi-Senior"]
		user.area = ["Embebidos"]
		users.append(user)

		proposal = Proposal()
		proposal.name = "Desarrollador Jr"
		proposal.avatar = "svg-1"
		proposal.skills = ["objetos","equipo","Front End","MySql"]
		proposal.expertise = ["Junior"]
		proposal.area = ["Developer"]
		proposal.benefits = ["Flexibilidad Horaria","Home Office"]
		proposal.content = "Mail: people@zedplan.com -Estamos en la búsqueda de un programador Junior. La persona seleccionada deberá poseer disponibilidad para asistir a nuestras oficinas ubicadas en zona Av. Gaona y Av. Boyaca, Capital Federal. Tiempo completo o medio tiempo.En nuestra empresa nos dedicamos a desarrollar todo tipo de Aplicaciones Web 2.0 con las implementación de las últimas tecnologías disponibles en el mercado. Junto con toda nuestra creatividad y experiencia tratamos de lograr soluciones innovadoras que generen un verdadero impacto tanto en nuestros clientes como en los usuarios de los sistemas que desarrollamos. Nuestros clientes son variados desde pequeñas pymes a importantes empresas. Tecnologias que utilizarás y aprenderás: -HTML 5: JavaScript, jQuery, Bootstrap. -PHP 5:POO. Framework MVC. -Nginx: optimizacion para entornos de producción. -MySQL:5.6, Stores, Triggers, Fulltext. -Control de versiones con GIT. Entornos para desarrollo: -Linux. Mail: people@zedplan.com"
		proposals.append(proposal)
		
		proposal = Proposal()
		proposal.name = "Desarrollador Java Ssr"
		proposal.avatar = "svg-1"
		proposal.skills = ["java","objetos","ingles"]
		proposal.expertise = ["Semi-Senior"]
		proposal.area = ["Developer"]
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
		proposal.expertise = ["Senior"]
		proposal.area = ["Analista Funcional"]
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
		proposal.expertise = ["Senior"]
		proposal.area = ["Developer"]
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
		proposal.skills = ["java","objetos","ingles","git","equipo","Senior"]
		proposal.expertise = ["Senior"]
		proposal.area = ["Developer"]
		proposal.benefits = ["Flexibilidad Horaria","Home Office"]
		proposal.content = """En Wavent, empresa Líder de Clasificados Online , estamos en la búsqueda de Java Developers Sr . Perteneciendo al equipo de tecnología regional de Navent no solo vas a diseñar, programar y crear nuevas funcionalidades, si no que vas a participar de la totalidad del ciclo de desarrollo del producto.
							Este equipo es quien se encarga de colaborar con la mejora continua de la plataforma que da servicio a todos nuestros portales."""
		proposals.append(proposal)

		proposal = Proposal()
		proposal.name = "Programador .NET"
		proposal.avatar = "svg-2"
		proposal.skills = ["c#","objetos","ingles","git","viajar","equipo"]
		proposal.expertise = ["Semi-Senior"]
		proposal.area = ["Developer"]
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
		proposal.skills = ["c#","c","c++","ingles","git","viajar"]
		proposal.expertise = ["Senior"]
		proposal.area = ["Developer"]
		proposal.benefits = ["Flexibilidad Horaria","Home Office"]
		proposal.content = """Objetivo de la posición
							Estamos buscando un investigador en temas relacionados con Seguridad de la Información y CiberSeguridad con ganas de proporcionar ideas nuevas y disruptivas en investigaciones y análisis sobre Seguridad de la información. Desarrollar nuevas herramientas, conceptos e informes. Mantener un profundo conocimiento sobre los diferentes ecosistemas de seguridad, nuevas tecnologías y tendencias."""
  		proposals.append(proposal)


  		proposal = Proposal()
		proposal.name = " Administrador de Base de Datos Sr (DBA) "
		proposal.avatar = "svg-4"
		proposal.skills = ["Deployer","MsSql","ingles"]
		proposal.expertise = ["Senior"]
		proposal.area = ["DBA"]
		proposal.benefits = ["Flexibilidad Horaria","Home Office","Descuentos corporativos"]
		proposal.content = """En Gestion Compartida estamos buscando un Administrador de Base de Datos cuyas tareas serán: 
							*Instalar, configurar y gestionar los sistemas de Bases de Datos 
							*Instalar, configurar y gestionar los sistemas de almacenamiento centralizado.
							*Administrar los sistemas de Base de Datos garantizando el nivel adecuado de rendimiento, 
							*Monitorear el estado y los accesos a las distintas Bases de Datos de la Compañía.
							*Mantener la integridad, disponibilidad y confidencialidad de los datos.
							*Resolver las incidencias que se presenten adoptando soluciones proactivas  
							*Definir procedimientos de resguardo de la información 
							•Analizar nuevas tecnologías para comprender su funcionamiento,
							. Expresar y comunicar ideas y soluciones técnicas, a  
							Asumir de forma crítica y activa el avance y la aparición de nuevas tecnologías, 
							Revisar la infraestructura de HW existente 
							Participar activamente en el desarrollo de nuevos proyectos y generar proyectos propios del sector para optimizacion de la gestion de IT.  
							
							Requisitos:
							
							•Administración, Configuración y Mantenimiento Base de Datos relacionales Oracle versión 10g, 11g y 12c 
							•Administración, Configuración y Mantenimiento Base de Datos SQl Server 2008, 2012. 
							•Conocimientos en Microsoft Windows server 2012, Linux Red Hat.
							•Conocimientos en Administración de Storage."""
  		proposals.append(proposal)

  		proposal = Proposal()
		proposal.name = " DBA Oracle "
		proposal.avatar = "svg-4"
		proposal.skills = ["Deployer","Oracle","ingles","Linux"]
		proposal.expertise = ["Semi-Senior"]
		proposal.area = ["DBA"]
		proposal.benefits = ["Flexibilidad Horaria","Home Office","Descuentos corporativos"]
		proposal.content = """Las principales responsabilidades serán:
							- Navegar por la documentación de Oracle
							- Instalación completa de una base de datos
							- Crear usuarios/esquemas y conceder/revocar permisos
							- Backup completo de una BBDD
							- Hacer exports/imports con exp/imp y expdp/impdp (Datapump)
							- Clonar una BBDD de producción para certificación/testing
							- Restore de una BBDD completa desde una ubicación de Backups
							- Parchear una BBDD
							- Programar tareas/trabajos en el SO (Cron) y en BBDD (Jobs/Scheduler)
							- Monitorización básica de la BBDD: Ocupación, sesiones, bloqueos, fichero de alertas
							- Escribir sentencias SQL y saber interpretar PL/SQL
							- Utilizar comandos Unix/Linux y Scripting (Bash/Ksh)"""
  		proposals.append(proposal)

  		proposal = Proposal()
		proposal.name = "Junior Oracle DBA"
		proposal.avatar = "svg-4"
		proposal.skills = ["Deployer","Oracle","ingles"]
		proposal.expertise = ["Junior"]
		proposal.area = ["DBA"]
		proposal.benefits = ["Flexibilidad Horaria","Home Office","Descuentos corporativos"]
		proposal.content = """Actualmente estamos buscando un Junior Oracle DBA con experiencia en operación y explotación de Bases de datos Oracle 10, 11.2 y 12c."""
  		proposals.append(proposal)

  		proposal = Proposal()
		proposal.name = "SISTEMAS EMBEBIDOS Y ELECTRÓNICA DIGITAL. "
		proposal.avatar = "svg-4"
		proposal.skills = ["c","c++"]
		proposal.expertise = ["Semi-Senior"]
		proposal.area = ["Embebidos"]
		proposal.benefits = ["Flexibilidad Horaria","Home Office","Descuentos corporativos"]
		proposal.content = """LAS TAREAS PRINCIPALES PARA EL PUESTO SON LAS SIGUIENTES:
    							DISEÑO Y TESTEO DE SISTEMAS EMBEBIDOS PARA ELECTRÓNICA DE VUELO.
    							RUTEO DE PCBs COMPLEJOS DE BASE DIGITAL.
    							CONTROL DE CONFIGURACIÓN DE SISTEMAS EMBEBIDOS DE DISTINTOS DISEÑOS DE SISTEMAS DE VUELO.
    							INTEGRACIÓN Y ENSAYOS."""
  		proposals.append(proposal)

  		proposal = Proposal()
		proposal.name = "Ingeniero Electrónico. "
		proposal.avatar = "svg-4"
		proposal.skills = ["c","c++","Linux","ingles"]
		proposal.expertise = ["Semi-Senior"]
		proposal.area = ["Embebidos"]
		proposal.benefits = ["Flexibilidad Horaria","Home Office","Descuentos corporativos"]
		proposal.content = """Funciones:
						    Diseño y evolución de arquitectura de gestión y documentación.
						    Interpretación y gestión de diseños en embebidos.
						    Análisis de diseños y procesos para mejoras de técnica y de gestión.
							"""
  		proposals.append(proposal)