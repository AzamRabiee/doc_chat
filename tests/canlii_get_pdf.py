import requests

case_page = "https://www.canlii.org/en/ab/abkb/doc/2025/2025abkb50/2025abkb50.html"
pdf_url = "https://www.canlii.org/en/ab/abkb/doc/2025/2025abkb50/2025abkb50.pdf"
output_file = "2025abkb50.pdf"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/121.0.0.0 Safari/537.36",
}

session = requests.Session()
session.headers.update(headers)

# Step 1: visit the HTML page to get cookies
session.get(case_page, timeout=30)

# Step 2: download the PDF using the same session
response = session.get(pdf_url, stream=True, timeout=30)
response.raise_for_status()

with open(output_file, "wb") as f:
    for chunk in response.iter_content(8192):
        f.write(chunk)

print("PDF downloaded successfully.")
