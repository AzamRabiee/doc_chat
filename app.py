import hashlib
import os
from pathlib import Path
from typing import Any, List, Optional, TypedDict

import gradio as gr

from agents.workflow import AgentWorkflow
from config import constants
from document_processor.file_handler import DocumentProcessor
from retriever.builder import RetrieverBuilder
from utils.logging import logger


class SessionState(TypedDict):
    file_hashes: List[str]  # JSON-friendly
    retriever: Optional[Any]


base_path = str(Path(__file__).parent)

EXAMPLES = {
    "2025abkb50": {
        "question": "Is the claim merit? Why?",
        "file_paths": [base_path + "/examples/2025abkb50.pdf"],
    },
    "2025bcsc427": {
        "question": "What is the case about?",
        "file_paths": [base_path + "/examples/2025bcsc427.pdf"],
    },
}

session_state = gr.State({"file_hashes": [], "retriever": None})


def main():
    processor = DocumentProcessor()
    retriever_builder = RetrieverBuilder()
    workflow = AgentWorkflow()

    # Define custom CSS for styling
    css = """
    .title {
        font-size: 1.5em !important; 
        text-align: center !important;
        color: #FFD700; 
    }

    .subtitle {
        font-size: 1em !important; 
        text-align: center !important;
        color: #FFD700; 
    }

    .text {
        text-align: center;
    }
    """

    with gr.Blocks(theme=gr.themes.Citrus(), title="DocChat 🐥", css=css) as demo:
        gr.Markdown(
            "## DocChat: powered by Docling 🐥 and LangGraph", elem_classes="subtitle"
        )
        gr.Markdown(
            "📤 Upload your PDF document, enter your query then hit Submit 📝, or you can select one of the examples from the drop-down menu.",
            elem_classes="text",
        )

        session_state = gr.State({"file_hashes": frozenset(), "retriever": None})

        # 3) Layout
        with gr.Row():
            with gr.Column():
                # Section for Examples
                gr.Markdown("### Example 📂")
                example_dropdown = gr.Dropdown(
                    label="Select an Example 🐥",
                    choices=list(EXAMPLES.keys()),
                    value=None,  # initially unselected
                )
                load_example_btn = gr.Button("Load Example 🛠️")

                # Standard input components
                files = gr.Files(
                    label="📄 Upload Documents", file_types=constants.ALLOWED_TYPES
                )
                # files = gr.Textbox(label="📄 Upload Documents")
                question = gr.Textbox(label="❓ Question", lines=3)

                submit_btn = gr.Button("Submit 🚀")

            with gr.Column():
                with gr.Tab("Answer"):
                    answer_output = gr.Markdown()
                with gr.Tab("Verification Report"):
                    verification_output = gr.Markdown()

        # 4) Helper function to load example into the UI
        def load_example(example_key: str):
            """
            Given a key like 'Example 1',
            read the relevant docs from disk and return
            them as file paths, plus the example question.
            """
            if not example_key or example_key not in EXAMPLES:
                return [], ""  # blank if not found

            ex_data = EXAMPLES[example_key]
            question = ex_data["question"]
            file_paths = ex_data["file_paths"]

            # Return file paths directly - gr.Files accepts paths
            loaded_files = []
            for path in file_paths:
                if os.path.exists(path):
                    loaded_files.append(path)
                else:
                    logger.warning(f"File not found: {path}")

            return loaded_files, question

        load_example_btn.click(
            fn=load_example, inputs=[example_dropdown], outputs=[files, question]
        )

        # 5) Standard flow for question submission
        def process_question(
            question_text: str, uploaded_files: List, state: SessionState
        ):
            try:
                if not question_text.strip():
                    raise ValueError("❌ Question cannot be empty")
                if not uploaded_files:
                    raise ValueError("❌ No documents uploaded")

                current_hashes = _get_file_hashes(uploaded_files)

                if state["retriever"] is None or current_hashes != state["file_hashes"]:
                    logger.info("Processing new/changed documents...")

                    all_chunks = []
                    for item in uploaded_files:
                        if isinstance(item, str):
                            file_path = item
                        elif isinstance(item, dict) and "path" in item:
                            file_path = item["path"]
                        else:
                            file_path = getattr(item, "path", None) or getattr(
                                item, "name", None
                            )
                        if not file_path:
                            continue

                        file_chunks = processor.process(file_path)
                        all_chunks.extend(file_chunks)

                    retriever = retriever_builder.build_hybrid_retriever(all_chunks)

                    state.update(
                        {"file_hashes": current_hashes, "retriever": retriever}
                    )

                result = workflow.full_pipeline(
                    question=question_text, retriever=state["retriever"]
                )
                
                # answer = f"""
                #     ## Answer 
                    
                #     {result["draft_answer"]}
                # """
                
                verifer_report = f"""
                    ## Verifier Report 
                    
                    {str(result["verification_report"])} 
                """

                return (
                    result["draft_answer"], 
                    verifer_report, 
                    state
                )

            except Exception as e:
                logger.error(f"Processing error: {str(e)}")
                return f"❌ Error: {str(e)}", "", state

        submit_btn.click(
            fn=process_question,
            inputs=[question, files, session_state],
            outputs=[answer_output, verification_output, session_state],
        )

    demo.launch(server_name="127.0.0.1", server_port=5000, share=True)


def _get_file_hashes(uploaded_files: List) -> List[str]:
    hashes = []
    for item in uploaded_files:
        # gr.Files may return str paths or FileData-like objects/dicts depending on Gradio version
        if isinstance(item, str):
            path = item
        elif isinstance(item, dict) and "path" in item:
            path = item["path"]
        else:
            path = getattr(item, "path", None) or getattr(item, "name", None)
        if not path:
            continue

        with open(path, "rb") as f:
            hashes.append(hashlib.sha256(f.read()).hexdigest())
    hashes.sort()
    return hashes


if __name__ == "__main__":
    main()
