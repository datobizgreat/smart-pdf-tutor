"""
PDF processing service - Phase 5
Handles PDF extraction and text processing
"""

from pypdf import PdfReader
from typing import Dict, List
import os


class PDFProcessor:
    """Handle PDF reading, text extraction, and chunking"""
    
    def extract_text(self, pdf_path: str) -> Dict:
        """
        Extract text from PDF and return with metadata
        
        Args:
            pdf_path: Path to PDF file
            
        Returns:
            Dictionary with extracted text and metadata
        """
        try:
            reader = PdfReader(pdf_path)
            total_pages = len(reader.pages)
            
            # Extract text from all pages
            full_text = ""
            pages_text = []
            
            for page_num, page in enumerate(reader.pages):
                text = page.extract_text()
                pages_text.append({
                    "page_number": page_num + 1,
                    "text": text
                })
                full_text += text + "\n"
            
            # Create preview (first 500 characters)
            preview = full_text[:500] + "..." if len(full_text) > 500 else full_text
            
            return {
                "total_pages": total_pages,
                "full_text": full_text,
                "pages": pages_text,
                "text_preview": preview
            }
            
        except Exception as e:
            raise Exception(f"Error extracting PDF: {str(e)}")
    
    def get_pages(self, pdf_path: str) -> List[Dict]:
        """
        Get individual pages from PDF
        
        Args:
            pdf_path: Path to PDF file
            
        Returns:
            List of pages with text content
        """
        reader = PdfReader(pdf_path)
        pages = []
        
        for page_num, page in enumerate(reader.pages):
            text = page.extract_text()
            pages.append({
                "page_number": page_num + 1,
                "text": text,
                "character_count": len(text)
            })
        
        return pages
    
    def split_into_chunks(self, text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
        """
        Split text into overlapping chunks - Phase 6
        
        Args:
            text: Full text to split
            chunk_size: Size of each chunk
            overlap: Overlap between chunks
            
        Returns:
            List of text chunks
        """
        chunks = []
        start = 0
        
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            chunks.append(chunk)
            start = end - overlap
        
        return chunks
