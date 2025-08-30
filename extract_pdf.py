#!/usr/bin/env python3
import pdfplumber
import sys

def extract_pdf_text(pdf_path):
    """Extract text from a PDF file using pdfplumber"""
    text_content = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_content += page_text + "\n\n"
        
        return text_content.strip()
    
    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return None

if __name__ == "__main__":
    pdf_path = "/Users/luis/projects/preparatic_web/pdfs/planContinuidad.pdf"
    content = extract_pdf_text(pdf_path)
    
    if content:
        print(content)
    else:
        print("Failed to extract content")