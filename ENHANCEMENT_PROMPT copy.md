# HTML FILE ENHANCEMENT PROMPT

## Base Enhancement Instructions

apply these comprehensive improvements to create a modern, interactive, and exam-focused study guide about 
this topic "Conceptos de sistemas operativos: Características, evolución y tendencias. Estructura, componentes y funciones. Sistemas operativos multiprocesador." in spanish
create a file html/sistemas-enhanced.html:

### 1. DARK/LIGHT MODE IMPLEMENTATION
- **Default to dark mode** (dark backgrounds, light text)
- Add toggle button in the top-right corner
- Use CSS custom properties for theme switching:
  ```css
  :root {
    --bg-primary: #1a1a1a;
    --bg-secondary: #2c2c2c;
    --text-primary: #e0e0e0;
    --text-secondary: #b0b0b0;
    --accent-color: #4a9eff;
  }
  [data-theme="light"] {
    --bg-primary: #ffffff;
    --bg-secondary: #f5f5f5;
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
- Break existing content into logical sections
- Enhance with detailed explanations
- Add visual elements (cards, timelines, diagrams)
- Include real-world examples and case studies
- Add comparison tables where appropriate

**Tab 6: Ejercicios Prácticos** (when applicable)
- For technical topics with calculations/problems
- 10 practical exercises with step-by-step solutions
- Interactive elements when possible
- Focus on exam-type scenarios
- Include difficulty levels (básico, intermedio, avanzado)

**Tab 7: Recursos y FAQ**
- Additional resources and references
- Frequently asked questions
- Best practices and recommendations
- Related tools and software
- Glossary of key terms

### 3. MODERN DESIGN IMPROVEMENTS
- **Typography**: Professional font hierarchy
- **Layout**: Responsive grid system
- **Colors**: Cohesive color scheme with proper contrast
- **Interactive Elements**:
  - Hover effects on buttons and cards
  - Smooth animations and transitions
  - Expandable sections
  - Progress indicators
  - Interactive navigation

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
- `original-file.html` → `original-file-enhanced.html`
- `tema_XX_topic.html` → `tema_XX_topic-enhanced.html`

### 7. VALIDATION REQUIREMENTS
Before completing each enhancement:
- Test dark/light mode toggle functionality
- Verify responsive design on mobile and desktop
- Check all tabs navigation works properly
- Validate HTML structure and accessibility
- Ensure all interactive elements function correctly
- Confirm localStorage persistence for theme preference

## Implementation Process
1. Read the original HTML file
2. Analyze existing content and structure
3. Apply all enhancements systematically
4. Create the new enhanced file
5. Update enhancement_tracking.json status to "completed"
6. Move to next file in queue

## Quality Checklist
- [ ] Dark mode is default with working toggle
- [ ] All 7 tabs are implemented with relevant content
- [ ] Exercises tab included for applicable topics
- [ ] Responsive design works on all screen sizes
- [ ] All interactive elements function properly
- [ ] Theme preference persists across sessions
- [ ] Content is comprehensive and exam-focused
- [ ] Spanish language throughout
- [ ] File saved with -enhanced suffix 

--- 