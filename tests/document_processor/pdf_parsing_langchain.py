"""
Test script for LangChain PDF parsing functionality.

This test verifies that LangChain's PyPDFLoader works correctly with PDF parsing,
text extraction, and page-level document handling.
"""

import sys
from pathlib import Path

# Add parent directory to path to import from app
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from langchain_community.document_loaders import PyPDFLoader


def test_pypdfloader_creation():
    """Test that PyPDFLoader can be created successfully."""
    print("\n🔍 Testing PyPDFLoader creation...")

    try:
        examples_dir = Path(__file__).parent.parent.parent / "examples"
        test_file = examples_dir / "2025abkb50.pdf"

        if not test_file.exists():
            print(f"⚠️  Test file not found: {test_file}, skipping test")
            return True

        loader = PyPDFLoader(str(test_file))
        assert loader is not None
        print("✅ PyPDFLoader created successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to create PyPDFLoader: {str(e)}")
        import traceback

        traceback.print_exc()
        return False


def test_langchain_pdf_loading():
    """Test that LangChain can load a PDF and extract pages."""
    print("\n🔍 Testing LangChain PDF loading...")

    try:
        examples_dir = Path(__file__).parent.parent.parent / "examples"
        test_file = examples_dir / "2025abkb50.pdf"

        if not test_file.exists():
            print(f"⚠️  Test file not found: {test_file}, skipping test")
            return True

        print(f"   Using test file: {test_file}")

        loader = PyPDFLoader(str(test_file))
        pages = loader.load()

        assert pages is not None
        assert len(pages) > 0
        print(f"✅ Successfully loaded PDF with {len(pages)} page(s)")
        return True
    except Exception as e:
        print(f"❌ Failed to load PDF: {str(e)}")
        import traceback

        traceback.print_exc()
        return False


def test_langchain_text_extraction():
    """Test that LangChain can extract text content from PDF pages."""
    print("\n🔍 Testing LangChain text extraction...")

    try:
        examples_dir = Path(__file__).parent.parent.parent / "examples"
        test_file = examples_dir / "2025abkb50.pdf"

        if not test_file.exists():
            print(f"⚠️  Test file not found: {test_file}, skipping test")
            return True

        print(f"   Using test file: {test_file}")

        loader = PyPDFLoader(str(test_file))
        pages = loader.load()

        # Extract text from all pages
        text = "\n\n".join([page.page_content for page in pages])

        assert text is not None
        assert len(text) > 0
        print(f"✅ Successfully extracted text ({len(text)} characters)")
        return True
    except Exception as e:
        print(f"❌ Failed to extract text: {str(e)}")
        import traceback

        traceback.print_exc()
        return False


def test_langchain_full_extraction():
    """Test full LangChain extraction workflow and print extracted content."""
    print("\n🔍 Testing full LangChain extraction workflow...")

    try:
        examples_dir = Path(__file__).parent.parent.parent / "examples"
        test_file = examples_dir / "2025abkb50.pdf"

        if not test_file.exists():
            print(f"⚠️  Test file not found: {test_file}, skipping test")
            return True

        print(f"   Using test file: {test_file}")

        # Load PDF using PyPDFLoader
        loader = PyPDFLoader(str(test_file))
        pages = loader.load()

        # Extract text from all pages
        print(f"   Number of Pages: {len(pages)}")
        text = "\n\n".join([page.page_content for page in pages])

        # Print full extracted content
        print("\n✅ Full Extracted Content (LangChain):\n")
        print(text)
        print("\n" + "=" * 100)

        assert pages is not None
        assert len(pages) > 0
        assert text is not None
        assert len(text) > 0
        print(f"✅ Full extraction workflow completed successfully")
        return True
    except Exception as e:
        print(f"❌ Failed full extraction workflow: {str(e)}")
        import traceback

        traceback.print_exc()
        return False


def test_langchain_with_ocr_pdf():
    """Test LangChain parsing with OCR PDF file."""
    print("\n🔍 Testing LangChain with OCR PDF...")

    try:
        examples_dir = Path(__file__).parent.parent.parent / "examples"
        test_file = examples_dir / "ocr_test.pdf"

        if not test_file.exists():
            print(f"⚠️  OCR test file not found: {test_file}, skipping test")
            return True

        print(f"   Using test file: {test_file}")

        loader = PyPDFLoader(str(test_file))
        pages = loader.load()

        text = "\n\n".join([page.page_content for page in pages])

        assert pages is not None
        assert len(pages) > 0
        print(
            f"✅ Successfully parsed OCR PDF with {len(pages)} page(s), {len(text)} characters"
        )
        return True
    except Exception as e:
        print(f"❌ Failed to parse OCR PDF: {str(e)}")
        import traceback

        traceback.print_exc()
        return False


def test_langchain_page_metadata():
    """Test that LangChain pages contain metadata."""
    print("\n🔍 Testing LangChain page metadata...")

    try:
        examples_dir = Path(__file__).parent.parent.parent / "examples"
        test_file = examples_dir / "2025abkb50.pdf"

        if not test_file.exists():
            print(f"⚠️  Test file not found: {test_file}, skipping test")
            return True

        print(f"   Using test file: {test_file}")

        loader = PyPDFLoader(str(test_file))
        pages = loader.load()

        # Check that pages have metadata
        for idx, page in enumerate(pages):
            assert hasattr(page, "metadata")
            assert hasattr(page, "page_content")
            if idx == 0:  # Just check first page
                print(f"   Page {idx + 1} metadata: {page.metadata}")
                print(
                    f"   Page {idx + 1} content length: {len(page.page_content)} characters"
                )

        print(f"✅ All {len(pages)} pages contain metadata and content")
        return True
    except Exception as e:
        print(f"❌ Failed to verify page metadata: {str(e)}")
        import traceback

        traceback.print_exc()
        return False


def main():
    """Run all tests."""
    print("=" * 80)
    print("🧪 Running LangChain PDF Parsing Tests")
    print("=" * 80)

    results = []

    # Run tests
    results.append(("Loader Creation", test_pypdfloader_creation()))
    results.append(("PDF Loading", test_langchain_pdf_loading()))
    results.append(("Text Extraction", test_langchain_text_extraction()))
    results.append(("Page Metadata", test_langchain_page_metadata()))
    results.append(("Full Extraction Workflow", test_langchain_full_extraction()))
    results.append(("OCR PDF Parsing", test_langchain_with_ocr_pdf()))

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
