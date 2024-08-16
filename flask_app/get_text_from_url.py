import requests
import fitz

import warnings
warnings.filterwarnings("ignore")

def get_text_from_url(url):
    pdf_data = []
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        pdf_doc = fitz.open(stream=response.content, filetype="pdf")
        for page_num in range(len(pdf_doc)):
          page = pdf_doc.load_page(page_num)
          text = page.get_text()
          pdf_data.append(text)

        pdf_doc.close()
    except requests.exceptions.Timeout:
        pdf_data.append("The request timed out.")
    except requests.exceptions.HTTPError as http_err:
        pdf_data.append(f"HTTP error occurred: {http_err}")
    except Exception as err:
        pdf_data.append(f"An error occurred: {err}")
    return "\n".join(pdf_data)  # Join all the pages' text into a single string
