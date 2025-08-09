# PreparaTIC - Centro de Estudios Interactivo

## Project Overview

This project is a web-based study center for preparing for technology-related exams and certifications. It provides interactive HTML guides on various topics like Agile methodologies, Cybersecurity, Cloud Computing, Data Science, Legal Frameworks, etc. The main interface is `index.html`, which serves as a dashboard showing available topics and overall progress. Individual study guides are generated as HTML files (from PDF sources) and stored in the `html/` directory. The `progress.json` file tracks which topics have been completed.

## Key Files and Directories

- `index.html`: Main dashboard page. Shows statistics, categories, and links to individual topic guides. Features a search bar and visual indicators for completed/coming-soon topics.
- `progress.json`: Tracks the status (completed or not) of study topics derived from PDF files in the `pdfs/` directory.
- `html/`: Directory containing the generated interactive HTML study guides for each topic.
- `pdfs/`: Directory containing the source PDF files for the study topics.
- `exams/`: Directory containing past exam papers and solutions.

## Directory Usage

This directory contains all the materials for the PreparaTIC study center. The workflow involves:
1.  Adding new source material as PDFs in the `pdfs/` directory.
2.  Running a process (as defined in `prd.md`) to convert these PDFs into interactive HTML guides in the `html/` directory.
3.  Updating `progress.json` to reflect the status of each topic.
4.  The `index.html` file automatically reflects the progress and provides navigation to the study guides.

## Development and Building

This is a client-side web project. It consists of static HTML, CSS, and JavaScript files. There is no build process required; simply open `index.html` in a web browser. The HTML guides in the `html/` directory are self-contained single files with embedded CSS and JS.

### Process for Adding New Topics

Based on the instructions in `prd.md`:
1.  Place a new PDF in the `pdfs/` directory.
2.  Create a corresponding interactive HTML file in the `html/` directory. This file should follow the structure and design principles outlined in the prompt within `prd.md` (modern design, tab system, interactive components, etc.).
3.  Add an entry for the new topic in `progress.json`, setting `completed` to `true` or `false`.
4.  Add a corresponding card in `index.html` under the appropriate category, linking to the new HTML file and reflecting its completion status.

### Updating the Homepage

The homepage (`index.html`) needs to be manually updated to:
- Add new topic cards.
- Update the "Temas Disponibles", "Completados", and "En Desarrollo" statistics in the header.
- Mark topics as "available" or "coming-soon" and update the "progress-indicator" and `onclick` links.

The `progress.json` file indicates which topics are completed (`completed: true`) and which are pending (`completed: false`). This should be used to update the homepage status. As of the last update (`2025-08-09`), there are 17 completed topics and 26 pending topics, matching the stats on the homepage.