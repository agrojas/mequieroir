/**
 * Proposals DataService
 * Uses embedded, hard-coded data model; acts asynchronously to simulate
 * remote data service call(s).
 *
 * @returns {{loadAll: Function}}
 * @constructor
 */
function ProposalsDataService($q) {
  var Proposals = [
    {
      name: "Desarrollador Java Ssr",
      avatar: "svg-1",
      phone: "111-2222",
      skills: ["java","objetos","ingles","git","viajar","equipo"],
      benefits: ["flexibilidadHoraria","homeOffice","bonoObjetivo"],
      content: "IT Company se encuentra en la búsqueda de un Desarrollador Java Ssr. para sumarse al equipo de una importante empresa de seguros. \
                Tareas/Responsabilidades: \
                ·         Desarrollo de requerimientos. \
                ·   Atender los pedidos de los usuarios sobre las aplicaciones a cargo, darle solución o adecuación. \
                ·         Posicionarse en el puesto tomando rápidamente el control de las aplicaciones. \
                ·         Comprender las necesidades de los usuarios y del negocio. \
                Requisitos del puesto: \
                ·         Orientamos la búsqueda a estudiante o graduado de sistemas. \
                ·         Contar con al menos 2 años de experiencia en posiciones similares."
    },
    {
      name: "Analista Funcional",
      avatar: "svg-2",
      phone: "111-2222",
      skills: ["analisis","ingles","git","viajar","equipo"],
      benefits: ["flexibilidadHoraria","homeOffice","bonoObjetivo","capacitacion"],
      content: "Tareas y funciones:Interpretar, analizar y documentar requerimientos de Areas Internas y clientes externos. \
                -Interpretar, analizar documentación Técnica y funcional. \
                -Participar en la elaboración de Propuestas de solución a los requerimientos recibidos. Principalmente orientadas a Desarrollo de Recaudaciones en\
                Aplicaciones integradas a la línea de caja de las Entidades y a través de canales electrónicos.\
                -Elaborar documentación para Areas Internas y Clientes Externos"
    },
    {
      name: "Ingeniero de Desarrollo",
      avatar: "svg-3",
      phone: "111-2222",
      skills: ["c","c++","c#","java","php","angular","cobol","objetos","ingles","git","viajar","equipo"],
      benefits: ["flexibilidadHoraria","homeOffice","bonoObjetivo","capacitacion"],
      content: "Ingeniero de Desarrollo \
                  Las responsabilidades del puesto serán:\
                  Controlar la contratación de servicios tecnológicos de la compañía\
                  Realizar el análisis, diseño, desarrollo e implementación de aplicaciones de la compañía\
                  Controlar el óptimo desempeño de las aplicaciones del negocio\
                  Evaluar viabilidad técnica y económica en la adquisición de herramientas\
                  Participar en la planificación y desarrollo de los requisitos relacionados con la ejecución de los proyectos tecnológicos\
                  Trabajar en conjunto con los contratistas de distintos servicios en la resolución de los problemas técnicos de los productos.\
                  Realizar seguimiento a los indicadores de gestión, e implementar mejoras de ser necesario\
                  Establecer mecanismos de control para tratar el producto o servicio no conforme"
    },
    {
      name: "Desarrollador Java Sr",
      avatar: "svg-4",
      phone: "111-2222",
      skills: ["c","c++","c#","java","php","angular","cobol","objetos","ingles","git","viajar","equipo"],
      benefits: ["flexibilidadHoraria","homeOffice","bonoObjetivo","capacitacion"],
      content: "En Wavent, empresa Líder de Clasificados Online , estamos en la búsqueda de Java Developers Sr .\ Perteneciendo al equipo de tecnología regional de Navent no solo vas a diseñar, programar y crear nuevas funcionalidades, si no que vas a participar de la totalidad del ciclo de desarrollo del producto.\
Este equipo es quien se encarga de colaborar con la mejora continua de la plataforma que da servicio a todos nuestros portales."
    },
    {
      name: "Programador .NET",
      avatar: "svg-2",
      phone: "111-2222",
      skills: ["c","c++","c#","java","php","angular","cobol","objetos","ingles","git","viajar","equipo"],
      benefits: ["flexibilidadHoraria","homeOffice","bonoObjetivo","capacitacion"],
      content: "IT Resources se encuentra en la búsqueda de un Programador .Net para sumarse al equipo de una importante cadena de mayoristas.\
                Tareas/Responsabilidades:\
                Desarrollo y Mantenimiento evolutivo .NET y de interfaces con periféricos (POSNET/Impresoras Fiscales).\
                Análisis de nuevos requerimientos\
                Documentación.\
                Requisitos excluyentes:\
                Orientamos la búsqueda a estudiantes en curso o graduados de Sistemas.\
                Contar con al menos 2 años de experiencia en posiciones similares.\
                Capacidad de análisis de procesos y diseño de soluciones."
    },
    {
      name: "Especialista en seguridad de la informacion y ciberseguridad",
      avatar: "svg-4",
      phone: "111-2222",
      skills: ["c","c++","c#","java","php","angular","cobol","objetos","ingles","git","viajar","equipo"],
      benefits: ["flexibilidadHoraria","homeOffice","bonoObjetivo","capacitacion"],
      content: "Objetivo de la posición\
  Estamos buscando un investigador en temas relacionados con Seguridad de la Información y CiberSeguridad con ganas de proporcionar ideas nuevas y disruptivas en investigaciones y análisis sobre Seguridad de la información. Desarrollar nuevas herramientas, conceptos e informes. Mantener un profundo conocimiento sobre los diferentes ecosistemas de seguridad, nuevas tecnologías y tendencias."
    }
  ];

  // Promise-based API
  return {
    loadAllProposals: function() {
      // Simulate async nature of real remote calls
      return $q.when(Proposals);
    }
  };
}

export default ["$q", ProposalsDataService];

