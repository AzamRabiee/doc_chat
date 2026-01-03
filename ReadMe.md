---
title: DocChat
sdk: gradio
python_version: "3.11"
app_file: app.py
---

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