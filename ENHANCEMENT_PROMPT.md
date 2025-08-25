# HTML FILE CREATION PROMPT

## Base Creation Instructions

**PDF Processing Workflow:**
1. Read pdfs_list.py to find the first file with `processed: False`
2. Select the first unprocessed PDF file
3. Read the PDF content of the file selected directly from the pdfs/ folder
4. Create a comprehensive, modern, interactive, and exam-focused study guide based solely on the PDF content
5. Save the enhanced HTML file in the html2/ folder
6. Update pdfs_list.py to mark the file as `processed: True`

**Important**: All content must come from the PDF being processed. Do not research external sources or look at existing HTML files.

Put all new files in the html2 folder that exists, dont check if it exists.

Limit the output of each new file to 30000 tokens maximum and name files using the PDF filename as base: `[pdf_filename_without_extension]-enhanced.html`


### 1. DARK/LIGHT MODE IMPLEMENTATION
- **Default to dark mode** (dark backgrounds, light text)
- Add toggle button in the top-right corner
- Use CSS custom properties for theme switching:
  ```css
  :root {
    --bg-primary: #0f0f0f;
    --bg-secondary: #1a1a1a;
    --bg-card: #252525;
    --bg-hover: #2f2f2f;
    --border-color: rgba(255, 255, 255, 0.1);
    --text-primary: #e0e0e0;
    --text-secondary: #b0b0b0;
    --accent-color: #4a9eff;
  }
  [data-theme="light"] {
    --bg-primary: #ffffff;
    --bg-secondary: #f5f5f5;
    --bg-card: #f8f9fa;
    --bg-hover: #e9ecef;
    --border-color: rgba(0, 0, 0, 0.1);
    --text-primary: #333333;
    --text-secondary: #666666;
    --accent-color: #0066cc;
  }
  ```
- Smooth transitions (0.3s ease) between themes
- Persist user preference in localStorage

### 2. ENHANCED CONTENT STRUCTURE
Transform the existing content into a comprehensive 7-tab system:

**Tab 1: Resumen General**
- Executive summary of the topic
- Key statistics and important numbers
- Main concepts overview
- Learning objectives

**Tab 2-5: Main Content Sections**
- Break PDF content into logical sections
- Enhance with detailed explanations from the PDF
- Add visual elements (cards, timelines, diagrams)
- Include real-world examples and case studies from the PDF
- Add comparison tables where appropriate from PDF content

**Tab 6: Ejercicios Prácticos**
- Create exam-style multiple choice questions (about 20 questions)
- Base questions primarily on PDF content, no external search is allowed for creating additional relevant exam questions
- Mark correct answers clearly for study purposes  
- Present in interactive quiz format with immediate feedback
- Include difficulty levels (básico, intermedio, avanzado)
- Focus on concepts likely to appear in public administration exams

**Tab 7: Recursos y FAQ**
- Glossary of key terms

### 3. MODERN DESIGN IMPROVEMENTS
- **Typography**: Professional font hierarchy
- **Layout**: Responsive grid system
- **Colors**: Cohesive color scheme with proper contrast
- **Card Design**:
  - Use `--bg-card` for card backgrounds to create subtle contrast
  - Apply `--border-color` for subtle borders when needed
  - Use `--bg-hover` for hover states on interactive elements
  - Cards should have subtle shadows for depth: `box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3)` (dark mode) / `rgba(0, 0, 0, 0.1)` (light mode)
- **Interactive Elements**:
  - Hover effects on buttons and cards using `--bg-hover`
  - Smooth animations and transitions (0.3s ease)
  - Expandable sections with visual feedback
  - Progress indicators with accent colors
  - Interactive navigation with proper contrast

### 4. TECHNICAL ENHANCEMENTS
- **Mobile-first responsive design**
- **Performance optimizations**:
  - Minified embedded CSS and JS
  - Optimized loading order
  - Lazy loading for heavy content
- **Accessibility improvements**:
  - ARIA labels and roles
  - Keyboard navigation support
  - High contrast ratios
  - Screen reader compatibility

### 5. CONTENT QUALITY STANDARDS
- **Spanish language throughout**
- **Exam-focused content**:
  - Emphasize concepts likely to appear in public administration exams
  - Include mnemonics and memory aids
  - Provide practice questions format
- **Technical accuracy**:
  - Up-to-date information
  - Industry standards compliance
  - Cross-references to official documentation

### 6. FILE NAMING CONVENTION
Save enhanced files with `-enhanced.html` suffix:


### 7. VALIDATION REQUIREMENTS
Before completing each enhancement:
- Validate HTML structure and accessibility

## Implementation Process
1. Read pdfs_list.py to find files with `processed: False`
2. Select the first unprocessed PDF file
3. Read the PDF content directly of the unprocessed file from the pdfs/ folder
4. Structure PDF content into the 7-tab system
5. For Tab 6 (Ejercicios Prácticos): External search is allowed to create relevant exam questions
6. Apply all design and technical enhancements
7. Create the new enhanced file in html2/ folder using PDF filename as base
8. Update pdfs_list.py to mark the file as `processed: True`

## Quality Checklist
- [ ] Dark mode is default with working toggle
- [ ] All 7 tabs are implemented with relevant content
- [ ] 20 exam-style questions with marked correct answers included
- [ ] Spanish language throughout
- [ ] File saved with -enhanced suffix
- [ ] pdfs_list.py updated with processed: True

---

**Usage**: When user says "continue", proceed with the next unprocessed PDF in pdfs_list.py and create a complete study guide based on the PDF content of this file that you will have to read, with external search allowed specifically for creating relevant exam questions in Tab 6.