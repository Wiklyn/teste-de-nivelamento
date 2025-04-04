import os
import requests
import zipfile
from bs4 import BeautifulSoup

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

DOWNLOAD_DIR = "01-web_scraping/pdf_files"
ZIP_FILE = "01-web_scraping/pdf_files.zip"

FILES_NAMES_TO_BE_DOWNLOADED = ["Anexo I", "Anexo II"]


def find_correct_links(soup):
    pdf_links = []

    for link in soup.find_all(
        "a", href=True
    ):
        text_in_link = link.get_text(strip=True)
        href = link["href"]

        if (
            any(name in text_in_link for name in FILES_NAMES_TO_BE_DOWNLOADED)
            and href.lower().endswith(".pdf")
        ):
            pdf_links.append(href)

    return pdf_links


def download_pdf_files(pdf_links):
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    for pdf_link in pdf_links:
        pdf_url = pdf_link if pdf_link.startswith(
            "http") else f"{URL}/{pdf_link}"
        nome_arquivo = pdf_url.split("/")[-1]
        pdf_path = os.path.join(DOWNLOAD_DIR, nome_arquivo)

        response = requests.get(pdf_url)
        with open(pdf_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {pdf_path}")


def zip_files(files_directory, final_directory):
    with zipfile.ZipFile(final_directory, "w") as zipf:
        for root, _, files in os.walk(files_directory):
            for file in files:
                zipf.write(os.path.join(root, file), file)
    print(f"Files zipped in: {final_directory}")


response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
pdf_links = find_correct_links(soup)

if pdf_links:
    download_pdf_files(pdf_links)
    zip_files(DOWNLOAD_DIR, ZIP_FILE)
else:
    print("No PDF file was found.")
