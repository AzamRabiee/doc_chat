"""
Test script for Gradio gr.Files component functionality.

This test verifies that gr.Files works correctly with file uploads,
file path handling, and integration with the document processing pipeline.
"""

import os
import sys
from pathlib import Path

# Add parent directory to path to import from app
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import gradio as gr

from config import constants
from document_processor.file_handler import DocumentProcessor


def test_files_component_creation():
    """Test that gr.Files component can be created successfully."""
    print("\n🔍 Testing gr.Files component creation...")

    try:
        files_component = gr.Files(label="Test Upload Documents")
        assert files_component is not None
        assert files_component.label == "Test Upload Documents"
        print("✅ gr.Files component created successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to create gr.Files component: {str(e)}")
        return False


def test_files_with_file_types():
    """Test that gr.Files component can be created with file_types parameter."""
    print("\n🔍 Testing gr.Files with file_types parameter...")

    try:
        # Test with file types (may cause the schema error we're trying to avoid)
        files_component = gr.Files(
            label="Test Upload", file_types=constants.ALLOWED_TYPES
        )
        assert files_component is not None
        print("✅ gr.Files with file_types created successfully")
        return True
    except Exception as e:
        print(f"⚠️  gr.Files with file_types failed (expected if schema bug): {str(e)}")
        return False


def test_files_without_file_types():
    """Test that gr.Files component works without file_types parameter."""
    print("\n🔍 Testing gr.Files without file_types parameter...")

    try:
        files_component = gr.Files(label="Test Upload Documents")
        assert files_component is not None
        print("✅ gr.Files without file_types created successfully")
        return True
    except Exception as e:
        print(f"❌ Failed to create gr.Files component: {str(e)}")
        return False


def test_files_in_blocks():
    """Test that gr.Files can be used in a Blocks interface."""
    print("\n🔍 Testing gr.Files in Blocks interface...")

    try:

        def process_files(uploaded_files):
            """Dummy function to process files."""
            if uploaded_files is None:
                return "No files uploaded"
            return f"Received {len(uploaded_files)} file(s)"

        with gr.Blocks() as demo:
            files = gr.Files(label="Upload Files")
            output = gr.Textbox()

            files.change(fn=process_files, inputs=files, outputs=output)

        assert demo is not None
        print("✅ gr.Files works in Blocks interface")
        return True
    except Exception as e:
        print(f"❌ Failed to create Blocks with gr.Files: {str(e)}")
        import traceback

        traceback.print_exc()
        return False


def test_files_with_actual_file():
    """Test gr.Files with an actual file from samples directory."""
    print("\n🔍 Testing gr.Files with actual file path...")

    try:
        # Get a test file from samples
        samples_dir = Path(__file__).parent / "samples"
        test_files = list(samples_dir.glob("*.pdf"))

        if not test_files:
            print("⚠️  No PDF files found in samples directory, skipping test")
            return True

        test_file = test_files[0]
        print(f"   Using test file: {test_file}")

        # Create a simple interface to test file handling
        def handle_file(uploaded_files):
            if uploaded_files is None or len(uploaded_files) == 0:
                return "No files"

            # uploaded_files should be a list of file paths
            file_paths = (
                uploaded_files if isinstance(uploaded_files, list) else [uploaded_files]
            )

            # Verify file exists
            for file_path in file_paths:
                if not os.path.exists(file_path):
                    return f"File not found: {file_path}"

            return f"Successfully processed {len(file_paths)} file(s)"

        with gr.Blocks() as demo:
            files = gr.Files(label="Upload Files")
            output = gr.Textbox()

            files.change(fn=handle_file, inputs=files, outputs=output)

        # Simulate file input (in a real test, you'd interact with the UI)
        # For now, just verify the component is set up correctly
        assert demo is not None
        print("✅ gr.Files setup works with file paths")
        return True

    except Exception as e:
        print(f"❌ Failed to test with actual file: {str(e)}")
        import traceback

        traceback.print_exc()
        return False


def test_files_integration_with_processor():
    """Test that file paths from gr.Files work with DocumentProcessor."""
    print("\n🔍 Testing gr.Files integration with DocumentProcessor...")

    try:
        samples_dir = Path(__file__).parent / "samples"
        test_files = list(samples_dir.glob("*.pdf"))

        if not test_files:
            print("⚠️  No PDF files found in samples directory, skipping test")
            return True

        test_file = str(test_files[0])
        print(f"   Using test file: {test_file}")

        processor = DocumentProcessor()

        # Simulate what would happen when gr.Files returns file paths
        # gr.Files returns a list of file paths (strings)
        file_paths = [test_file]

        # Process the file (this is what happens in process_question)
        chunks = processor.process(file_paths[0])

        assert chunks is not None
        assert len(chunks) > 0
        print(
            f"✅ Successfully processed file through DocumentProcessor: {len(chunks)} chunks"
        )
        return True

    except Exception as e:
        print(f"❌ Failed integration test: {str(e)}")
        import traceback

        traceback.print_exc()
        return False


def test_files_api_info_generation():
    """Test that Blocks with gr.Files can generate API info without errors."""
    print("\n🔍 Testing API info generation with gr.Files...")

    try:

        def dummy_fn(files):
            return "OK"

        with gr.Blocks() as demo:
            files = gr.Files(label="Test")
            output = gr.Textbox()
            files.change(fn=dummy_fn, inputs=files, outputs=output)

        # Try to get API info (this is where the schema error occurs)
        try:
            demo.get_api_info()
            print("✅ API info generated successfully")
            return True
        except TypeError as e:
            if "argument of type 'bool' is not iterable" in str(e):
                print(
                    "❌ Schema generation error detected (the bug we're trying to fix)"
                )
                print(f"   Error: {str(e)}")
                return False
            else:
                raise

    except Exception as e:
        print(f"❌ Failed API info test: {str(e)}")
        import traceback

        traceback.print_exc()
        return False


def main():
    """Run all tests."""
    print("=" * 80)
    print("🧪 Running gr.Files Component Tests")
    print("=" * 80)

    results = []

    # Run tests
    results.append(("Component Creation", test_files_component_creation()))
    results.append(("Files without file_types", test_files_without_file_types()))
    results.append(("Files in Blocks", test_files_in_blocks()))
    results.append(("Files with actual file", test_files_with_actual_file()))
    results.append(
        ("Integration with Processor", test_files_integration_with_processor())
    )
    results.append(("API Info Generation", test_files_api_info_generation()))
    results.append(
        ("Files with file_types", test_files_with_file_types())
    )  # Test last as it may fail

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
