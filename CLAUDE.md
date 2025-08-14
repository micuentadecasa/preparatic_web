# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a web-based study guide project that processes PDF documents and converts them into interactive HTML pages. The project aims to create a modern, interactive learning platform for various technical topics in Spanish.

## Project Structure

```
preparatic_web/
├── pdfs/          # Source PDF documents on various technical topics
├── prd.md         # Product requirements document with HTML template
├── temas.py       # List of 50 themes to be processed
├── progress.json  # Progress tracking file
└── CLAUDE.md      # This file
```

## Key Development Tasks

### Creating HTML Pages for All Themes

**CURRENT TASK**: Create HTML pages for all 50 themes listed in `temas.py` with the following requirements:

1. **Dark/Light Mode Functionality**
   - Dark mode as default
   - Toggle button to switch between modes
   - Persist user preference in localStorage

2. **Content Sources**
   - Use information from PDFs when available (enhance and expand the content)
   - Use AI knowledge to fill gaps where PDF information is insufficient
   - Ensure all content is comprehensive and exam-focused

3. **Enhanced Tab Structure**
   - Tab 1: Overview - General introduction with key statistics
   - Tab 2-5: Main content sections specific to the topic
   - Tab 6: **Exercises** - 10 calculation/problem-solving exercises (when applicable)
   - Tab 7: Resources/FAQ/Special section

### HTML Template Requirements

Each HTML page should follow the template specified in `prd.md` with these additions:
- **Dark/Light Mode Support**
  - CSS variables for easy theme switching
  - Dark theme as default (dark backgrounds, light text)
  - Light theme as alternative
  - Smooth transitions between modes
- Single HTML file with embedded CSS and JavaScript
- Tab-based navigation system
- Mobile-responsive design
- Interactive components (tabs, animations, hover effects)

### Content Structure for Each Topic

Each HTML page should include:
- Tab 1: Overview - General introduction with key statistics
- Tab 2-5: Main content sections specific to the topic
- Tab 6: **Exercises Tab** (NEW)
  - Only include if the theme involves calculations or problem-solving
  - 10 practical exercises with solutions
  - Focus on exam-type problems
  - Interactive elements when possible
- Tab 7: Resources/FAQ/Special section
- Visual components: cards, timelines, statistics grids
- Spanish language content

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

## Development Guidelines

### When Creating HTML Pages

1. Use the HTML template structure from `prd.md` with dark/light mode enhancements
2. Ensure all content is in Spanish
3. Create self-contained HTML files (CSS and JS embedded)
4. **Dark Mode Implementation**:
   - Use CSS custom properties (--variables) for colors
   - Dark theme as default: dark backgrounds (#1a1a1a, #2c2c2c), light text (#e0e0e0, #ffffff)
   - Light theme: light backgrounds (#ffffff, #f5f5f5), dark text (#333333, #000000)
   - Smooth transitions (0.3s ease) between theme changes
5. Make pages mobile-responsive
6. Include interactive elements (tabs, animations)
7. **Exercises Tab**: Add for themes that involve calculations or technical problem-solving

### Themes Requiring Exercises Tab

Themes that should include calculation/problem exercises:
- Tema 4: Inteligencia de Negocios (OLTP/OLAP calculations)
- Tema 21: Diseño de Bases de Datos (normalization exercises)
- Tema 22: Estructuras de Datos y Algoritmos (algorithm complexity)
- Tema 33: Minería de Datos y Big Data (data processing calculations)
- Tema 35: Cloud Computing (resource allocation calculations)
- Tema 38: Control de Ejecución (performance calculations)
- Tema 39: Almacenamiento de Datos (capacity planning)
- Tema 40-42: Redes (network calculations, IP addressing)
- Tema 44: Redes Conmutadas (bandwidth calculations)
- And others with technical/quantitative content

### Progress Tracking

**Use `progress.json`** to track:
- Which themes have been processed (out of 50 total)
- Theme number, title, and completion status
- Last update date for each HTML file
- Exercises included (true/false)
- Source used (PDF info + AI knowledge)

### File Organization

- **HTML files**: `tema_XX.html` (e.g., `tema_01.html`, `tema_02.html`)
- **Homepage**: `index.html` with links to all 50 themes
- **PDFs**: Keep in `pdfs/` folder as reference
- **Tracking**: `progress.json` for completion status

### Content Development Process

1. **Read theme definition** from `temas.py`
2. **Check for relevant PDFs** in `pdfs/` folder
3. **Extract and enhance PDF content** when available
4. **Fill knowledge gaps** using AI knowledge
5. **Create exercises** for calculation-heavy themes
6. **Implement dark/light mode** with proper CSS variables
7. **Test functionality** (tabs, theme toggle, responsive design)
8. **Update progress tracking**

## Testing

Since this is a static HTML project, testing involves:
- Opening HTML files in a browser to verify rendering
- **Testing dark/light mode toggle** and persistence
- Checking responsive design on different screen sizes
- Verifying all tabs and interactive elements work correctly
- **Testing exercises functionality** when included
- Ensuring all links in the index page work
- Validating Spanish content accuracy