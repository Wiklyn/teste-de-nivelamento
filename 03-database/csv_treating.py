import chardet
import shutil
import os

ORIGINAL_CSV_FILES_DIR = "03-database/csv_files/original_csv_files"
TREATED_CSV_FILES_DIR = "03-database/csv_files/treated_csv_files"
DEM_CONT = "demonstracoes_contabeis"
OP_ATV = "operadoras_ativas"


def copy_files(original_dir: str, final_dir: str):
    os.makedirs(final_dir, exist_ok=True)

    for file_name in os.listdir(original_dir):
        file_path = os.path.join(original_dir, file_name)

        if os.path.isfile(file_path):
            shutil.copy2(file_path, final_dir)


def verify_file_encoding(file_path, file_name):
    with open(file_path, "rb") as f:
        raw_data = f.read(100000)
        result = chardet.detect(raw_data)

    print(f"File: {file_name}. Encoding: {result['encoding']}")


def remove_quotes_from_csv_headers(csv_file_path: str):
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    lines[0] = lines[0].replace('"', '')

    with open(csv_file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

    print(f'Quotes removed from headers: {csv_file_path}')


def lowercase_csv_headers(csv_file_path: str):
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    lines[0] = lines[0].lower()

    with open(csv_file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

    print(f"Column headers converted to lowercase: {csv_file_path}")


def replace_comma_with_dot_in_csv(csv_file_path: str):
    with open(csv_file_path, "r", encoding="utf-8") as file:
        content = file.read()

    content = content.replace(",", ".")

    with open(csv_file_path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Modified file saved in: {csv_file_path}")


# Essa parte tá bem mal escrita. Fui ficando sem tempo para pensar em como
# fazer a refatoração

copy_files(f"{ORIGINAL_CSV_FILES_DIR}/{DEM_CONT}",
           f"{TREATED_CSV_FILES_DIR}/{DEM_CONT}")

for file_name in os.listdir(f"{TREATED_CSV_FILES_DIR}/{DEM_CONT}"):
    if file_name.endswith(".csv"):
        file_path = os.path.join(
            f"{TREATED_CSV_FILES_DIR}/{DEM_CONT}", file_name
        )
        verify_file_encoding(file_path, file_name)
        remove_quotes_from_csv_headers(file_path)
        lowercase_csv_headers(file_path)
        replace_comma_with_dot_in_csv(file_path)
        print()


copy_files(f"{ORIGINAL_CSV_FILES_DIR}/{OP_ATV}",
           f"{TREATED_CSV_FILES_DIR}/{OP_ATV}")

for file_name in os.listdir(f"{TREATED_CSV_FILES_DIR}/{OP_ATV}"):
    if file_name.endswith(".csv"):
        file_path = os.path.join(
            f"{TREATED_CSV_FILES_DIR}/{OP_ATV}", file_name
        )
        verify_file_encoding(file_path, file_name)
        lowercase_csv_headers(file_path)
        replace_comma_with_dot_in_csv(file_path)
        print()
