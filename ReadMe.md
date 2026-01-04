---
title: Doc Chat
emoji: 📈
colorFrom: yellow
colorTo: red
sdk: gradio
sdk_version: 6.2.0
python_version: "3.11"
app_file: app.py
pinned: false
short_description: An Agentic AI APP with LangGraph and Docling
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

## Run the app
```
source .venv/bin/activate
python app.py
```

## Run a single test
For example for `test_files_api_info_generation`
```
python -m pytest tests/document_processor/file_upload.py::test_files_api_info_generation
```

## TODO
- huggingface spaces

