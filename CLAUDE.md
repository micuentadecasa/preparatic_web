# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a web-based study guide project that processes PDF documents and converts them into interactive HTML pages. The project aims to create a modern, interactive learning platform for various technical topics in Spanish.

## Project Structure

```
preparatic_web/
├── pdfs/          # Source PDF documents on various technical topics
├── prd.md         # Product requirements document with HTML template
└── CLAUDE.md      # This file
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

### Content Structure for Each Topic

Each HTML page should include:
- Tab 1: Overview - General introduction with key statistics
- Tab 2-5: Main content sections specific to the topic
- Tab 6: Resources/FAQ/Special section
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

1. Use the exact HTML template structure from `prd.md`
2. Ensure all content is in Spanish
3. Create self-contained HTML files (CSS and JS embedded)
4. Follow the specified color palette and design requirements
5. Make pages mobile-responsive
6. Include interactive elements (tabs, animations)

### Progress Tracking

Consider creating a `progress.json` or similar file to track:
- Which PDFs have been processed
- Which are pending
- Last update date for each HTML file

### File Organization

- Place all generated HTML files in the root directory or a dedicated folder (e.g., `html/`)
- Keep the homepage (`index.html`) in the root directory
- Maintain the original PDFs in the `pdfs/` folder

## Testing

Since this is a static HTML project, testing involves:
- Opening HTML files in a browser to verify rendering
- Checking responsive design on different screen sizes
- Verifying all tabs and interactive elements work correctly
- Ensuring all links in the index page work