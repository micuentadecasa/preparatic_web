# QWEN.md

This file provides guidance to Qwen Code when working with code in this repository.

## Project Overview

This is a web-based study guide project that processes PDF documents and converts them into interactive HTML pages. The project aims to create a modern, interactive learning platform for various technical topics in Spanish, specifically tailored for exam preparation.

## Project Structure

```
preparatic_web/
├── pdfs/          # Source PDF documents on various technical topics
├── html/          # Generated HTML study guides
├── prd.md         # Product requirements document with HTML template
├── index.html     # Homepage with index linking to all topic pages
├── progress.json  # Tracks which PDFs have been processed
└── QWEN.md        # This file
```

## Key Development Tasks

### Processing PDFs and Creating HTML Pages

1. **Analyze each PDF** in the `pdfs/` folder and create a corresponding HTML file in Spanish
2. **Create a homepage** (`index.html`) with an index linking to all topic pages
3. **Track progress** - maintain a way to know which PDFs have been processed

### HTML Template Requirements

Each HTML page should follow the template specified in `prd.md`:
- Single HTML file with embedded CSS and JavaScript
- Tab-based navigation system
- Specific color palette (Primary: #3498db, Secondary: #2c3e50, etc.)
- Mobile-responsive design
- Interactive components (tabs, animations, hover effects)
- **Dark mode by default** with light mode toggle

### Content Structure for Each Topic

Each HTML page should include:
- Tab 1: Overview - General introduction with key statistics
- Tab 2-5: Main content sections specific to the topic with exam-focused details
- Tab 6: Resources/FAQ/Special section
- Visual components: cards, timelines, statistics grids
- Spanish language content
- **Detailed exam preparation information**
- **Comprehensive exercises with detailed solutions**

## Theme-Based Processing System

In addition to processing PDFs, we will now create HTML pages based on the following themes list. For each theme:

1. Check if there's already an HTML file in the `html/` folder with relevant information
2. If an HTML exists, use it as a base for the new theme-based HTML
3. If no HTML exists, create a new one following the template from `prd.md`
4. For themes with exercises (like networking), add a tab with interactive exercises
5. Name files as `tema-{number}.html` with appropriate titles
6. **Include detailed exam preparation content with key points to remember**
7. **Include comprehensive exercises with detailed explanations of solutions**

## PDF Topics to Process

The following PDFs need to be converted to HTML study guides:
- AGIL.pdf - Agile methodologies
- CIFRADO.pdf - Encryption
- OSI.pdf - OSI model
- PKI.pdf - Public Key Infrastructure
- SGDB.pdf - Database management systems
- JAVA.pdf - Java programming
- actos administrativos.pdf - Administrative acts
- agilismo.pdf - Agile practices
- auditoria.pdf - Auditing
- ciberseguridad.pdf - Cybersecurity
- cloud.pdf - Cloud computing
- contratos.pdf - Contracts
- empleadopublico.pdf - Public employment
- ens.pdf - National Security Scheme
- itil.pdf, itil 2.pdf - ITIL framework
- metrica.pdf, metrica v3.pdf - METRICA methodology
- protecciondatos.pdf - Data protection
- redes.pdf - Networks
- seguridad_redes.pdf - Network security
- virtualization.pdf - Virtualization
- And others in the pdfs/ folder

## Theme List for Processing

### I. Tecnología Básica
1. Tecnologías actuales de ordenadores: de los dispositivos móviles a los superordenadores y arquitecturas escalables y de altas prestaciones. Computación en la nube. Base tecnológica. Componentes, funcionalidades y capacidades.
2. Conceptos de sistemas operativos: Características, evolución y tendencias. Estructura, componentes y funciones. Sistemas operativos multiprocesador.
3. Características técnicas y funcionales de los sistemas operativos: Windows, Linux, Unix y otros. Sistemas operativos para dispositivos móviles.
4. Inteligencia de negocios: cuadros de mando integral, sistemas de soporte a las decisiones, sistemas de información ejecutiva y almacenes de datos. OLTP y OLAP.
5. Sistemas de gestión de bases de datos relacionales: características y elementos constitutivos. Antecedentes históricos. El lenguaje SQL. Estándares de conectividad: ODBC y JDBC.
6. Arquitectura de sistemas cliente-servidor y multicapas: tipología. Componentes. Interoperabilidad de componentes. Ventajas e inconvenientes. Arquitectura de servicios web.
7. Lenguajes de marca o etiqueta. Características y funcionalidades. SGML, HTML, XML y sus derivaciones. Lenguajes de script.
8. Análisis y gestión de riesgos de los sistemas de información. La metodología MAGERIT: método, elementos y técnicas.
9. Auditoría Informática: objetivos, alcance y metodología. Técnicas y herramientas. Normas y estándares. Auditoría del ENS y de protección de datos. Auditoría de seguridad física.
10. Gestión de la atención a clientes y usuarios: centros de contacto, CRM. ERP. Arquitectura multicanal. Sistemas de respuesta de voz interactiva (IVR). Voice XML.
11. Seguridad física y lógica de un sistema de información. Herramientas en ciberseguridad. Gestión de incidentes. Informática forense.
12. Software libre y software propietario. Características y tipos de licencias. La protección jurídica de los programas de ordenador. Tecnologías de protección de derechos digitales.
13. Técnicas de evaluación de alternativas y análisis de viabilidad. Personal, procedimientos, datos, software y hardware. Presupuestación y control de costes de un proyecto informático.
14. Documática. Gestión y archivo electrónico de documentos. Sistemas de gestión documental y de contenidos. Sindicación de contenido. Sistemas de gestión de flujos de trabajos. Búsqueda de información: robots, spiders, otros. Posicionamiento y buscadores (SEO).

### II. Desarrollo de Sistemas
15. Concepto del ciclo de vida de los sistemas y fases. Modelos de ciclo de vida.
16. Gestión del proceso de desarrollo: objetivos, actores y actividades. Técnicas y prácticas de gestión de proyectos.
17. Planificación del desarrollo. Técnicas de planificación. Metodologías de desarrollo. Metodologías ágiles: Scrum, Kanban y Lean Developement.
18. Estrategias de determinación de requerimientos: entrevistas, derivación de sistemas existentes, análisis y prototipos. La especificación de requisitos de software.
19. Análisis estructurado. Diagramas de flujo de datos. Diagramas de estructura. Diccionario de datos. Flujogramas.
20. Modelización conceptual. El modelo Entidad/Relación extendido (E/R): elementos. Reglas de modelización. Validación y construcción de modelos de datos.
21. Diseño de bases de datos. La arquitectura ANSI/SPARC. El modelo lógico relacional. Normalización. Diseño lógico. Diseño físico. Problemas de concurrencia de acceso. Mecanismos de resolución de conflictos.
22. Tipos abstractos de datos y estructuras de datos. Grafos. Tipos de algoritmos: ordenación y búsqueda. Estrategias de diseño de algoritmos. Organizaciones de ficheros.
23. Diseño de programas. Diseño estructurado. Análisis de transformación y de transacción. Cohesión y acoplamiento.
24. Construcción del sistema. Entornos de construcción y generación de código. Estándares de documentación. Manuales de usuario y manuales técnicos. Formación de usuarios y personal técnico: métodos y materiales.
25. Pruebas. Planificación y documentación. Utilización de datos de prueba. Pruebas de software, hardware, procedimientos y datos.
26. Instalación y cambio. Estrategias de sustitución. Recepción e instalación. Evaluación post-implementación. Mantenimiento.
27. Análisis y diseño orientado a objetos. Elementos. El proceso unificado de software. El lenguaje de modelado unificado (UML). Patrones de diseño.
28. La arquitectura Java EE. La plataforma .Net. Ecosistema Python. Elementos constitutivos. Productos y herramientas.
29. Buenas prácticas en el desarrollo software y operaciones. DevOps, SecOps y MLOps.
30. Aplicaciones web. Diseño web multiplataforma/multidispositivo. Desarrollo web front-end y en servidor. Tecnologías de programación: JavaScript, applets, servlets, ASP, JSP y PHP. Servicios web: estándares, protocolos asociados, interoperabilidad y seguridad. Internacionalización y localización.
31. La calidad del software y su medida. Modelos, métricas, normas y estándares.
32. Accesibilidad, diseño universal y usabilidad. Accesibilidad y usabilidad de las tecnologías, productos y servicios relacionados con la sociedad de la información. Experiencia de Usuario o UX.
33. Minería de datos. Aplicación a la resolución de problemas de gestión. Tecnología y algoritmos. Procesamiento analítico en línea (OLAP). Big data. Deep Learning. Machine Learning. Bases de datos NoSQL.

### III. Sistemas y Comunicaciones
34. Administración del sistema operativo y software de base. Administración de sistemas de gestión de bases de datos. Funciones y responsabilidades.
35. Cloud Computing. IaaS, PaaS, SaaS. Nubes privadas, públicas e híbridas.
36. Prácticas de mantenimiento de equipos e instalaciones. Tipos de mantenimiento. Monitorización y gestión de capacidad.
37. Gestión de la configuración. Gestión de librerías de programas y de medios magnéticos. Control de cambios y de versiones. Los lenguajes de control de trabajos. Las técnicas y herramientas de operación automática.
38. Control de la ejecución de los trabajos. Evaluación del rendimiento. Planificación de la capacidad. Análisis de la carga. Herramientas y técnicas utilizables.
39. Almacenamiento masivo de datos. Sistemas SAN, NAS y DAS: componentes, protocolos, gestión y administración. Virtualización del almacenamiento. Gestión de volúmenes.
40. Redes locales. Tipología. Técnicas de transmisión. Métodos de acceso. Dispositivos de interconexión.
41. Administración de redes locales. Gestión de usuarios. Gestión de dispositivos. Monitorización y control de tráfico. Gestión SNMP. Gestión de incidencias.
42. El modelo TCP/IP y el modelo de referencia de interconexión de sistemas abiertos (OSI) de ISO: arquitectura, capas, interfaces, protocolos, direccionamiento y encaminamiento. Principales protocolos de la arquitectura de comunicaciones TCP/IP.
43. Planificación física de un centro de tratamiento de la información. Vulnerabilidades, riesgo y protección. Dimensionamiento de equipos. Factores a considerar. Virtualización de plataforma y de recursos. Virtualización de puestos de trabajo.
44. Redes conmutadas y de difusión. Conmutación de circuitos y de paquetes. Integración voz-datos. Protocolos de encaminamiento. Ethernet conmutada. MPLS. Calidad de servicio (QOS).
45. La seguridad en redes. Seguridad perimetral. Control de accesos. Técnicas criptográficas y protocolos seguros. Mecanismos de firma digital. Redes privadas virtuales. Seguridad en el puesto del usuario.
46. La red Internet: arquitectura de red. Principios de funcionamiento. Servicios: evolución, estado actual y perspectivas de futuro. La web semántica. Internet de las Cosas (IoT). Edge computing. BlockChain.
47. Tecnología XDSL y telecomunicaciones por cable: concepto, características y normativa reguladora.
48. Redes de nueva generación y servicios convergentes (NGN/IMS). VoIP, ToIP y comunicaciones unificadas. Convergencia telefonía fija-telefonía móvil.
49. Sistemas de comunicaciones móviles. Generaciones. Sistemas celulares. Trunking. Soluciones de gestión de dispositivos móviles (MDM). Redes inalámbricas. Protocolos. Características funcionales y técnicas. Seguridad. Normativa reguladora.
50. IP móvil y PLC (Power Line Comunications). Características técnicas. Modos de operación. Seguridad. Normativa reguladora. Ventajas e inconvenientes. Televisión digital. Servicios de televisión (IPTV y OTT). Radiodifusión sonora digital.

## Development Guidelines

### When Creating HTML Pages

1. Use the exact HTML template structure from `prd.md`
2. Ensure all content is in Spanish
3. Create self-contained HTML files (CSS and JS embedded)
4. Follow the specified color palette and design requirements
5. Make pages mobile-responsive
6. Include interactive elements (tabs, animations)
7. When creating theme-based HTMLs, check if there's existing content in the `html/` folder that can be leveraged
8. For themes with exercises (like networking calculations), add interactive components in a dedicated tab
9. **Include detailed exam preparation content with key points to remember**
10. **Include comprehensive exercises with detailed explanations of solutions**
11. **Dark mode by default** with light mode toggle

### Critical Workflow Step: PDF Review Process

**After creating each HTML theme file, ALWAYS follow this enhancement process:**

1. **Check for relevant PDFs** in the `pdfs/` folder that relate to the theme
2. **Review the PDF content** thoroughly to identify:
   - Additional technical details not included in the initial HTML
   - Specific terminology, definitions, or standards mentioned
   - Examples, case studies, or practical applications
   - Diagrams, charts, or visual elements that could be described
   - Exercise examples or practice questions
   - References to regulations, laws, or official standards
3. **Enhance the HTML file** by adding the missing information:
   - Incorporate technical details from the PDFs
   - Add specific examples mentioned in the PDFs
   - Include relevant standards or regulations
   - Expand on sections that were too brief
   - Add new exercises based on PDF examples
4. **Verify completeness** by ensuring the HTML now covers:
   - All major concepts from the PDFs
   - Technical specifications and details
   - Practical applications and examples
   - Exam-relevant information
   - Sufficient exercises with detailed solutions

This process ensures that each theme HTML is comprehensive and draws from all available source material.

### Progress Tracking

Update `progress.json` to track:
- Which PDFs have been processed
- Which are pending
- Last update date for each HTML file
- Track theme-based HTML creation separately
- **Track which themes have been completed with detailed content and exercises**

### File Organization

- Place all generated HTML files in the `html/` folder
- Keep the homepage (`index.html`) in the root directory
- Maintain the original PDFs in the `pdfs/` folder
- Theme-based HTML files should be named `tema-{number}.html`

## Theme Development Progress

### Completed Themes (with detailed exam content and exercises):
- Tema 5: Bases de Datos Relacionales - Created with detailed information about normalization, Codd rules, and comprehensive exercises
- Tema 40: Redes Locales - Created with detailed networking exercises, comparison of OSI vs TCP/IP, and subnetting exercises

### Themes In Progress:
- Tema 42: Modelo TCP/IP y OSI - Will be enhanced with more detailed comparison and exercises

### Pending Themes:
All other themes (1-4, 6-39, 41, 43-50) need to be created with the following requirements:
1. Detailed exam preparation content with key points to remember
2. Comprehensive exercises with detailed explanations of solutions
3. Dark mode enabled by default with light mode toggle
4. Content based on the specific theme description
5. Leveraging existing HTML content where relevant (e.g., using OSI.html content for networking themes)
6. Creating specific exercises for technical themes (subnet calculations for networking, normalization for databases, etc.)
7. **Enhanced with information from relevant PDFs in the pdfs/ folder**

## Content Requirements for Each Theme

### Exam Preparation Focus
Each theme HTML should include:
- Key concepts that are frequently tested in exams
- Common question patterns and how to approach them
- Important definitions and terminology
- Practical examples and use cases
- Comparison tables for similar concepts
- Flowcharts or diagrams where applicable

### Exercise Requirements
Each theme should include:
- Multiple choice questions with detailed explanations
- Practical calculation exercises (where applicable)
- Scenario-based questions
- True/False questions with explanations
- Fill-in-the-blank exercises
- **Detailed solutions with step-by-step explanations**

### Content Structure for Theme HTMLs
1. **Overview Tab**: 
   - Key statistics related to the theme
   - Brief introduction with exam relevance
   - Main concepts checklist

2. **Content Tabs (2-4)**:
   - Detailed explanations of core concepts
   - Exam-focused details and key points
   - Common pitfalls and misconceptions
   - Comparison tables and diagrams
   - Practical examples

3. **Resources Tab**:
   - Related standards and regulations
   - Useful links and references
   - FAQ section with exam tips

4. **Exercises Tab**:
   - Multiple types of exercises
   - Detailed solutions and explanations
   - Scoring system for self-evaluation

## Implementation Notes

### Dark Mode by Default
All HTML files should:
- Have dark mode as the default theme
- Include a toggle button in the top-right corner
- Use appropriate color schemes for both modes
- Ensure good contrast and readability in both modes

### Leveraging Existing Content
When creating theme HTMLs:
- Check existing HTML files in the `html/` folder for relevant content
- Adapt and integrate existing content where appropriate
- Maintain consistency with existing design and structure
- Enhance with additional exam-focused information

### Exercise Development
For each theme, create exercises that:
- Test understanding of key concepts
- Include practical calculations where relevant
- Provide detailed solutions with explanations
- Help identify common mistakes
- Build confidence for exam scenarios

### Special Focus Areas by Theme Type
- **Networking Themes** (40-50): Subnetting calculations, protocol comparisons, OSI/TCP-IP layer functions
- **Database Themes** (5, 20, 21): Normalization exercises, Codd rules, SQL syntax
- **Security Themes** (8, 9, 11, 45): Encryption methods, risk assessment techniques, security models
- **Development Themes** (15-30): SDLC models, design patterns, programming concepts
- **Systems Themes** (1-4, 34-39): System architecture, virtualization, cloud models

## Templates and Examples

### Available Templates:
1. `html/tema-template.html` - Original template
2. `html/tema-template-dark.html` - Template with dark mode as default
3. `html/tema-5-detail.html` - Detailed example for databases with normalization and Codd rules
4. `html/tema-40-detail.html` - Detailed example for networking with subnetting and OSI/TCP-IP comparison

### Best Practices from Examples:
- Include formulas and calculation methods for technical topics
- Provide step-by-step solutions for exercises
- Use visual elements like tables and diagrams to explain complex concepts
- Include exam tips and common mistakes to avoid
- Create realistic exam scenarios in exercises
- **Enhance with information extracted from relevant PDFs**

## PDF Review Process Checklist

For each theme, after initial HTML creation, perform this review:

### 1. PDF Identification
- [ ] List all PDFs in `pdfs/` folder that relate to this theme
- [ ] Note specific pages or sections that are relevant

### 2. Content Enhancement
- [ ] Add technical specifications found in PDFs
- [ ] Include specific terminology and definitions
- [ ] Incorporate examples and case studies
- [ ] Add references to standards, laws, or regulations
- [ ] Expand on sections that were too brief

### 3. Exercise Development
- [ ] Create exercises based on PDF examples
- [ ] Add scenario-based questions from PDF case studies
- [ ] Include True/False questions based on PDF statements
- [ ] Develop calculation exercises from PDF formulas

### 4. Completeness Verification
- [ ] Ensure all major PDF concepts are covered
- [ ] Verify technical accuracy against PDF sources
- [ ] Check that exam-relevant information is included
- [ ] Confirm exercises are varied and comprehensive

This process ensures that each theme HTML is not only comprehensive but also draws from all available authoritative sources.