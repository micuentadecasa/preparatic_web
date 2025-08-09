import os
import json
from temas import temas

# Read the template
with open('html/tema-template.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Function to get relevant existing HTML content for a theme
def get_relevant_html(theme_number, short_title):
    # Mapping of themes to potentially relevant existing HTML files
    theme_to_html = {
        1: ['cloud.html', 'sistemas.html'],  # Tecnologías de ordenadores y cloud
        2: ['sistemas.html'],  # Sistemas operativos
        3: ['sistemas.html'],  # Sistemas operativos específicos
        4: ['ciencia.html'],  # Inteligencia de negocios
        5: ['sgdb.html'],  # Bases de datos relacionales
        6: ['cliente-servidor.html'],  # Arquitectura cliente-servidor
        7: ['lenguajes-marca.html'],  # Lenguajes de marca
        8: ['riesgos.html'],  # Gestión de riesgos
        9: ['auditoria.html'],  # Auditoría informática
        10: [],  # Gestión de atención a clientes
        11: ['ciberseguridad.html', 'seguridad-redes.html'],  # Seguridad de sistemas
        12: [],  # Software libre y propietario
        13: [],  # Evaluación de alternativas
        14: [],  # Documática
        15: [],  # Ciclo de vida de sistemas
        16: ['gestion-proyectos.html'],  # Gestión de procesos
        17: ['agil.html', 'agilismo.html'],  # Planificación y metodologías ágiles
        18: [],  # Determinación de requerimientos
        19: [],  # Análisis estructurado
        20: ['er.html'],  # Modelo Entidad/Relación
        21: ['sgdb.html'],  # Diseño de bases de datos
        22: [],  # Estructuras de datos y algoritmos
        23: [],  # Diseño de programas
        24: [],  # Construcción de sistemas
        25: [],  # Pruebas de sistemas
        26: [],  # Instalación y mantenimiento
        27: ['java.html'],  # Diseño orientado a objetos
        28: ['java.html'],  # Arquitecturas de desarrollo
        29: [],  # DevOps y buenas prácticas
        30: [],  # Aplicaciones web
        31: [],  # Calidad del software
        32: [],  # Accesibilidad y UX
        33: ['ciencia.html'],  # Minería de datos y big data
        34: ['sistemas.html'],  # Administración de sistemas
        35: ['cloud.html'],  # Cloud computing avanzado
        36: [],  # Mantenimiento de equipos
        37: ['cambios.html'],  # Gestión de configuración
        38: [],  # Control de ejecución
        39: [],  # Almacenamiento de datos
        40: ['redes.html'],  # Redes locales
        41: ['redes.html'],  # Administración de redes
        42: ['osi.html', 'redes.html'],  # Modelos TCP/IP y OSI
        43: ['centro-si.html'],  # Planificación de centros de datos
        44: ['redes.html'],  # Redes conmutadas
        45: ['seguridad-redes.html', 'ciberseguridad.html'],  # Seguridad en redes
        46: [],  # Internet y tecnologías emergentes
        47: [],  # Telecomunicaciones por cable
        48: [],  # Redes de nueva generación
        49: [],  # Comunicaciones móviles
        50: []  # Tecnologías de comunicación avanzadas
    }
    
    # For networking themes, we'll add specific exercises
    networking_themes = [40, 41, 42, 44, 45, 47, 48, 49, 50]
    
    # Generate theme-specific content
    content = {}
    
    # Basic info
    content['number'] = theme_number
    content['title'] = short_title
    content['overview_content'] = f"Esta guía cubre los aspectos fundamentales del tema {theme_number}: {short_title}."
    
    # Stats (varies by theme)
    if theme_number in networking_themes:
        content['stat1_number'] = "7"
        content['stat1_text'] = "Capas del modelo OSI"
        content['stat2_number'] = "4"
        content['stat2_text'] = "Tipos principales de redes"
        content['stat3_number'] = "99.9%"
        content['stat3_text'] = "Disponibilidad objetivo"
    elif theme_number in [5, 21]:
        content['stat1_number'] = "ACID"
        content['stat1_text'] = "Propiedades de las transacciones"
        content['stat2_number'] = "3"
        content['stat2_text'] = "Formas normales principales"
        content['stat3_number'] = "SQL"
        content['stat3_text'] = "Lenguaje de consulta estándar"
    elif theme_number in [1, 35]:
        content['stat1_number'] = "IaaS"
        content['stat1_text'] = "Infrastructure as a Service"
        content['stat2_number'] = "PaaS"
        content['stat2_text'] = "Platform as a Service"
        content['stat3_number'] = "SaaS"
        content['stat3_text'] = "Software as a Service"
    else:
        content['stat1_number'] = "100%"
        content['stat1_text'] = "Cobertura temática"
        content['stat2_number'] = "24/7"
        content['stat2_text'] = "Disponibilidad de recursos"
        content['stat3_number'] = "5★"
        content['stat3_text'] = "Calidad del contenido"
    
    # Key concepts (varies by theme)
    if theme_number in networking_themes:
        content['key_concept1'] = "Modelos de referencia OSI y TCP/IP"
        content['key_concept2'] = "Protocolos de comunicación"
        content['key_concept3'] = "Direccionamiento y enrutamiento"
        content['key_concept4'] = "Seguridad en redes"
        content['key_concept5'] = "Calidad de servicio (QoS)"
    elif theme_number in [5, 21]:
        content['key_concept1'] = "Modelo relacional"
        content['key_concept2'] = "Lenguaje SQL"
        content['key_concept3'] = "Normalización"
        content['key_concept4'] = "Transacciones ACID"
        content['key_concept5'] = "Índices y optimización"
    elif theme_number in [1, 35]:
        content['key_concept1'] = "Modelos de servicio en la nube"
        content['key_concept2'] = "Arquitecturas escalables"
        content['key_concept3'] = "Virtualización"
        content['key_concept4'] = "Seguridad en el cloud"
        content['key_concept5'] = "Gobernanza y compliance"
    else:
        content['key_concept1'] = "Conceptos fundamentales"
        content['key_concept2'] = "Mejores prácticas"
        content['key_concept3'] = "Consideraciones técnicas"
        content['key_concept4'] = "Aspectos de seguridad"
        content['key_concept5'] = "Aplicaciones prácticas"
    
    # Content titles and descriptions (generic but themed)
    content['content1_title'] = "Fundamentos y Conceptos Básicos"
    content['content1_description'] = f"Exploración detallada de los fundamentos del tema {theme_number}."
    content['content1_details_title'] = "Elementos Clave"
    content['content1_details'] = f"Los elementos clave del tema {theme_number} incluyen conceptos esenciales que todo profesional debe conocer."
    
    content['content2_title'] = "Implementación y Aplicación"
    content['content2_description'] = f"Cómo se aplica el tema {theme_number} en entornos reales."
    content['content2_details_title'] = "Comparativa de Enfoques"
    content['content2_details'] = f"Existen diferentes enfoques para implementar soluciones relacionadas con {short_title}."
    
    content['content3_title'] = "Consideraciones Avanzadas"
    content['content3_description'] = f"Aspectos avanzados y consideraciones especiales del tema {theme_number}."
    content['content3_details_title'] = "Factores Críticos"
    content['content3_details'] = f"Al trabajar con {short_title}, hay varios factores críticos que deben considerarse."
    
    # Timeline content (generic)
    content['timeline1_title'] = "Introducción"
    content['timeline1_description'] = f"Primera aparición y definición del concepto de {short_title}."
    content['timeline2_title'] = "Desarrollo"
    content['timeline2_description'] = f"Evolución y adopción generalizada de {short_title}."
    content['timeline3_title'] = "Madurez"
    content['timeline3_description'] = f"Estado actual y mejores prácticas en {short_title}."
    
    # Important points (generic)
    content['important_point1'] = "Comprender los fundamentos teóricos"
    content['important_point2'] = "Aplicar las mejores prácticas"
    content['important_point3'] = "Mantenerse actualizado con las tendencias"
    
    # Table content (generic)
    content['table_header1'] = "Aspecto"
    content['table_header2'] = "Descripción"
    content['table_header3'] = "Importancia"
    content['table_row1_col1'] = "Fundamentos"
    content['table_row1_col2'] = "Conceptos básicos del tema"
    content['table_row1_col3'] = "Alta"
    content['table_row2_col1'] = "Implementación"
    content['table_row2_col2'] = "Aplicación práctica"
    content['table_row2_col3'] = "Crítica"
    content['table_row3_col1'] = "Avanzado"
    content['table_row3_col2'] = "Consideraciones especiales"
    content['table_row3_col3'] = "Importante"
    
    # Considerations and best practices (generic)
    content['important_considerations'] = f"Al trabajar con {short_title}, es importante considerar múltiples factores que pueden afectar el resultado."
    content['best_practice1'] = "Seguir metodologías establecidas"
    content['best_practice2'] = "Documentar todos los procesos"
    content['best_practice3'] = "Realizar pruebas exhaustivas"
    
    # Resources (generic)
    content['resource1_title'] = "Documentación oficial"
    content['resource1_description'] = "Guías y manuales oficiales del tema"
    content['resource2_title'] = "Cursos especializados"
    content['resource2_description'] = "Programas de formación avanzada"
    content['resource3_title'] = "Comunidades profesionales"
    content['resource3_description'] = "Foros y grupos de expertos"
    content['resource4_title'] = "Herramientas recomendadas"
    content['resource4_description'] = "Software y aplicaciones especializadas"
    
    # Links (generic)
    content['link1_url'] = "https://es.wikipedia.org/wiki/" + short_title.replace(" ", "_")
    content['link1_text'] = "Wikipedia - " + short_title
    content['link2_url'] = "https://www.google.com/search?q=" + short_title.replace(" ", "+")
    content['link2_text'] = "Búsqueda en Google"
    content['link3_url'] = "https://github.com/topics/" + short_title.replace(" ", "-").lower()
    content['link3_text'] = "GitHub - Recursos relacionados"
    
    # FAQs (generic)
    content['faq1_question'] = f"¿Cuál es la importancia del tema {theme_number}?"
    content['faq1_answer'] = f"El tema {theme_number} ({short_title}) es fundamental para comprender los aspectos técnicos y prácticos de esta área."
    content['faq2_question'] = f"¿Cómo se aplica en la práctica el tema {theme_number}?"
    content['faq2_answer'] = f"En la práctica, {short_title} se aplica en diversos contextos profesionales para resolver problemas específicos."
    
    # Exercises description (generic)
    content['exercises_description'] = f"Practica tus conocimientos sobre {short_title} con estos ejercicios interactivos."
    
    # For networking themes, add specific exercises
    if theme_number == 40:  # Redes locales
        content['exercise1_title'] = "Cálculo de Subredes"
        content['exercise1_question'] = "¿Cuántas subredes se pueden crear con una máscara de subred /26?"
        content['exercise1_option_a'] = "2"
        content['exercise1_option_b'] = "4"
        content['exercise1_option_c'] = "6"
        content['exercise1_option_d'] = "8"
        content['exercise1_correct'] = "b"
        
        content['exercise2_title'] = "Identificación de Topologías"
        content['exercise2_question'] = "¿Qué topología de red tiene un punto de fallo único?"
        content['exercise2_correct'] = "Estrella"
        
        content['exercise3_title'] = "Cálculo de Direcciones"
        content['exercise3_question'] = "¿Cuántos hosts se pueden direccionar en una red /28?"
        content['exercise3_correct'] = "14"
    elif theme_number == 42:  # TCP/IP y OSI
        content['exercise1_title'] = "Capas del Modelo OSI"
        content['exercise1_question'] = "¿En qué capa del modelo OSI se encuentra el protocolo TCP?"
        content['exercise1_option_a'] = "Capa de Enlace"
        content['exercise1_option_b'] = "Capa de Red"
        content['exercise1_option_c'] = "Capa de Transporte"
        content['exercise1_option_d'] = "Capa de Aplicación"
        content['exercise1_correct'] = "c"
        
        content['exercise2_title'] = "Modelo TCP/IP"
        content['exercise2_question'] = "¿Cuántas capas tiene el modelo TCP/IP?"
        content['exercise2_correct'] = "4"
        
        content['exercise3_title'] = "Direccionamiento IP"
        content['exercise3_question'] = "¿Qué clase de dirección IP comienza con 110 en binario?"
        content['exercise3_correct'] = "Clase C"
    elif theme_number in networking_themes:
        # Generic networking exercise
        content['exercise1_title'] = "Conceptos de Redes"
        content['exercise1_question'] = "¿Cuál es el propósito principal de una red de computadoras?"
        content['exercise1_option_a'] = "Aumentar el costo de operación"
        content['exercise1_option_b'] = "Reducir la seguridad"
        content['exercise1_option_c'] = "Compartir recursos e información"
        content['exercise1_option_d'] = "Limitar el acceso a datos"
        content['exercise1_correct'] = "c"
        
        content['exercise2_title'] = "Protocolos de Red"
        content['exercise2_question'] = "¿Qué protocolo se utiliza para convertir nombres de dominio en direcciones IP?"
        content['exercise2_correct'] = "DNS"
        
        content['exercise3_title'] = "Seguridad en Redes"
        content['exercise3_question'] = "¿Qué significa el acrónimo VPN?"
        content['exercise3_correct'] = "Virtual Private Network"
    else:
        # Generic exercises for other themes
        content['exercise1_title'] = "Conceptos Fundamentales"
        content['exercise1_question'] = f"¿Cuál es el concepto principal del tema {theme_number}?"
        content['exercise1_option_a'] = "Concepto A"
        content['exercise1_option_b'] = "Concepto B"
        content['exercise1_option_c'] = "Concepto C"
        content['exercise1_option_d'] = "Concepto D"
        content['exercise1_correct'] = "b"
        
        content['exercise2_title'] = "Aplicación Práctica"
        content['exercise2_question'] = f"¿Cuál es una aplicación común de {short_title}?"
        content['exercise2_correct'] = "Aplicación específica"
        
        content['exercise3_title'] = "Mejores Prácticas"
        content['exercise3_question'] = f"¿Cuál es una consideración importante al trabajar con {short_title}?"
        content['exercise3_correct'] = "Consideración clave"
    
    return content

# Create HTML files for each theme
for tema in temas:
    # Get content for this theme
    content = get_relevant_html(tema['number'], tema['short_title'])
    
    # Fill template with content
    html_content = template
    for key, value in content.items():
        html_content = html_content.replace(f'{{{key}}}', str(value))
    
    # Write to file
    filename = f"tema-{tema['number']:02d}.html"
    filepath = os.path.join('html', filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Created {filename}")

print("All theme HTML files have been generated.")