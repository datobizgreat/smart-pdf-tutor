"""
Unit tests for PDF processor
Phase 5 testing
"""

import sys
import tempfile
import unittest
from pathlib import Path

from pypdf import PdfWriter

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from services.pdf_processor import PDFProcessor


class TestPDFProcessor(unittest.TestCase):
    
    def setUp(self):
        self.processor = PDFProcessor()

    def _create_sample_pdf(self, page_count: int = 2) -> Path:
        """Create a temporary PDF file for testing."""
        temp_file = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
        temp_file.close()
        pdf_path = Path(temp_file.name)

        writer = PdfWriter()
        for _ in range(page_count):
            writer.add_blank_page(width=72, height=72)

        writer.write(str(pdf_path))
        self.addCleanup(lambda: pdf_path.unlink(missing_ok=True))
        return pdf_path
    
    def test_split_into_chunks(self):
        """Test text chunking functionality"""
        text = "This is a sample text. " * 50
        chunks = self.processor.split_into_chunks(text, chunk_size=100, overlap=20)
        
        self.assertGreater(len(chunks), 0)
        self.assertLessEqual(len(chunks[0]), 100)

    def test_extract_text_returns_metadata(self):
        """Test that PDF text extraction returns page metadata and previews."""
        pdf_path = self._create_sample_pdf(page_count=2)

        result = self.processor.extract_text(str(pdf_path))

        self.assertEqual(result["total_pages"], 2)
        self.assertIn("full_text", result)
        self.assertIn("pages", result)
        self.assertIn("text_preview", result)
        self.assertEqual(len(result["pages"]), 2)

    def test_get_pages_returns_page_details(self):
        """Test that page retrieval returns page numbers and character counts."""
        pdf_path = self._create_sample_pdf(page_count=2)

        pages = self.processor.get_pages(str(pdf_path))

        self.assertEqual(len(pages), 2)
        self.assertEqual(pages[0]["page_number"], 1)
        self.assertEqual(pages[1]["page_number"], 2)
        self.assertIn("text", pages[0])
        self.assertIn("character_count", pages[0])


if __name__ == '__main__':
    unittest.main()
