"""
Test script for Docling PDF parsing functionality.

This test verifies that Docling DocumentConverter works correctly with PDF parsing,
markdown extraction, and text splitting using MarkdownHeaderTextSplitter.
"""

import sys
from pathlib import Path

# Add parent directory to path to import from app
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from docling.document_converter import DocumentConverter
from langchain_text_splitters import MarkdownHeaderTextSplitter


def test_docling_converter_creation():
    """Test that DocumentConverter can be created successfully."""
    print("\n🔍 Testing DocumentConverter creation...")

    try:
        converter = DocumentConverter()
        assert converter is not None
        print("✅ DocumentConverter created successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to create DocumentConverter: {str(e)}")
        import traceback

        traceback.print_exc()
        return False


def test_docling_pdf_parsing():
    """Test that Docling can parse a PDF and extract markdown."""
    print("\n🔍 Testing Docling PDF parsing...")

    try:
        # Get test file from examples directory
        examples_dir = Path(__file__).parent.parent.parent / "examples"
        test_file = examples_dir / "2025abkb50.pdf"

        if not test_file.exists():
            print(f"⚠️  Test file not found: {test_file}, skipping test")
            return True

        print(f"   Using test file: {test_file}")

        converter = DocumentConverter()
        result = converter.convert(str(test_file))
        markdown_document = result.document.export_to_markdown()

        assert markdown_document is not None
        assert len(markdown_document) > 0
        print(
            f"✅ Successfully parsed PDF and extracted markdown ({len(markdown_document)} characters)"
        )
        return True
    except Exception as e:
        print(f"❌ Failed to parse PDF: {str(e)}")
        import traceback

        traceback.print_exc()
        return False


def test_docling_with_markdown_splitting():
    """Test that Docling parsed content can be split using MarkdownHeaderTextSplitter."""
    print("\n🔍 Testing Docling with MarkdownHeaderTextSplitter...")

    try:
        examples_dir = Path(__file__).parent.parent.parent / "examples"
        test_file = examples_dir / "2025abkb50.pdf"

        if not test_file.exists():
            print(f"⚠️  Test file not found: {test_file}, skipping test")
            return True

        print(f"   Using test file: {test_file}")

        # Parse with Docling
        converter = DocumentConverter()
        result = converter.convert(str(test_file))
        markdown_document = result.document.export_to_markdown()

        # Define headers to split on
        headers_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
        ]

        # Initialize Markdown Splitter
        markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=headers_to_split_on
        )
        docs_list = markdown_splitter.split_text(markdown_document)

        assert docs_list is not None
        assert len(docs_list) > 0
        print(f"✅ Successfully split markdown into {len(docs_list)} sections")
        return True
    except Exception as e:
        print(f"❌ Failed to split markdown: {str(e)}")
        import traceback

        traceback.print_exc()
        return False


def test_docling_full_extraction():
    """Test full Docling extraction workflow and print extracted content."""
    print("\n🔍 Testing full Docling extraction workflow...")

    try:
        examples_dir = Path(__file__).parent.parent.parent / "examples"
        test_file = examples_dir / "2025abkb50.pdf"

        if not test_file.exists():
            print(f"⚠️  Test file not found: {test_file}, skipping test")
            return True

        print(f"   Using test file: {test_file}")

        # Initialize Docling Converter
        converter = DocumentConverter()
        result = converter.convert(str(test_file))
        markdown_document = result.document.export_to_markdown()

        # Define headers to split on
        headers_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
        ]

        # Initialize Markdown Splitter
        markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=headers_to_split_on
        )
        docs_list = markdown_splitter.split_text(markdown_document)

        # Print full extracted sections
        print(f"   Number of Sections: {len(docs_list)}")
        print("\n✅ Full Extracted Content (Docling):")
        for idx, doc in enumerate(docs_list):
            print(f"\n🔹 Section {idx + 1}:\n{doc}\n" + "-" * 80)

        assert docs_list is not None
        assert len(docs_list) > 0
        print(f"✅ Full extraction workflow completed successfully")
        return True
    except Exception as e:
        print(f"❌ Failed full extraction workflow: {str(e)}")
        import traceback

        traceback.print_exc()
        return False


def test_docling_with_ocr_pdf():
    """Test Docling parsing with OCR PDF file."""
    print("\n🔍 Testing Docling with OCR PDF...")

    try:
        examples_dir = Path(__file__).parent.parent.parent / "examples"
        test_file = examples_dir / "ocr_test.pdf"

        if not test_file.exists():
            print(f"⚠️  OCR test file not found: {test_file}, skipping test")
            return True

        print(f"   Using test file: {test_file}")

        converter = DocumentConverter()
        result = converter.convert(str(test_file))
        markdown_document = result.document.export_to_markdown()

        assert markdown_document is not None
        print(f"✅ Successfully parsed OCR PDF ({len(markdown_document)} characters)")
        return True
    except Exception as e:
        print(f"❌ Failed to parse OCR PDF: {str(e)}")
        import traceback

        traceback.print_exc()
        return False


def main():
    """Run all tests."""
    print("=" * 80)
    print("🧪 Running Docling PDF Parsing Tests")
    print("=" * 80)

    results = []

    # Run tests
    results.append(("Converter Creation", test_docling_converter_creation()))
    results.append(("PDF Parsing", test_docling_pdf_parsing()))
    results.append(("Markdown Splitting", test_docling_with_markdown_splitting()))
    results.append(("Full Extraction Workflow", test_docling_full_extraction()))
    results.append(("OCR PDF Parsing", test_docling_with_ocr_pdf()))

    # Print summary
    print("\n" + "=" * 80)
    print("📊 Test Summary")
    print("=" * 80)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")

    print(f"\nTotal: {passed}/{total} tests passed")
    print("=" * 80)

    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
