import os
import re
from typing import Dict, List, Tuple
import zipfile

import pandas as pd
import pdfplumber

PDF_FILE = "01-web_scraping/pdf_files/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
CSV_FILE_DIR = "02-data_treating/csv_files"
CSV_FILE_NAME = "extracted_data.csv"
CSV_FILE_PATH = f"{CSV_FILE_DIR}/{CSV_FILE_NAME}"
ZIP_FILE = "02-data_treating/Teste_wiklyn.zip"


def extract_table_and_subtitle(pdf_path: str) -> Tuple[List[List[str]], Dict]:
    full_table: List[List[str]] = []
    subs: Dict = {}
    header_replaced: bool = False

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            table = page.extract_table()
            if table:
                for row in table:
                    for i in range(len(row)):
                        if row[i]:
                            row[i] = row[i].replace('\n', ' ')

                if not header_replaced:
                    header = table[0]
                    header_replaced = True
                    for i, column in enumerate(header):
                        if column in subs:
                            header[i] = subs[column]
                    full_table.append(header)

                else:
                    table_data = table[1:]
                    full_table.extend(table_data)

                    for row in full_table:
                        for i in range(len(row)):
                            if row[i] in subs:
                                row[i] = subs[row[i]]

            page_text = page.extract_text()
            if page_text:
                subs_matches = re.findall(
                    r"(OD|AMB)\s*[:=]\s*([A-Za-z0-9_ ,\.]+(?:\s+[A-Za-z0-9_]+)*)",
                    page_text
                )
                for abbreviation, full in subs_matches:
                    subs[abbreviation.strip()] = full.strip()

    return full_table, subs


def replace_abbreviations(table: List[List[str]], subs: Dict):
    if not table:
        return []

    header = table[0]
    new_header = [subs.get(col, col) for col in header]

    treated_table = [new_header] + table[1:]
    return treated_table


def create_csv(table: List[List[str]], csv_file_name: str):
    os.makedirs(CSV_FILE_DIR, exist_ok=True)

    df = pd.DataFrame(table[1:], columns=table[0])
    df.to_csv(csv_file_name, index=False)
    print(f"Data saved in: {csv_file_name}")


def zip_files(files_directory: str, final_directory: str):
    with zipfile.ZipFile(final_directory, "w") as zipf:
        for root, _, files in os.walk(files_directory):
            for file in files:
                zipf.write(os.path.join(root, file), file)
    print(f"Files zipped in: {final_directory}")


table, subs = extract_table_and_subtitle(PDF_FILE)
treated_table = replace_abbreviations(table, subs)
create_csv(treated_table, CSV_FILE_PATH)
zip_files(CSV_FILE_PATH, ZIP_FILE)
