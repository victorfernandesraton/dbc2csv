import logging
from os import walk, path
import glob
import subprocess
from simpledbf import Dbf5

BLAST = "./bin/blast-dbf/blast-dbf"


def discover_files(dir: str, extension: str):
    files = []
    if not path.isdir(dir):
        raise FileNotFoundError

    for dirpath, _dirname, _filenames in walk(dir):
        read_files = glob.glob(path.join(dirpath, '*' + extension))
        for file in read_files:
            if file.endswith(f".{extension}"):
                files.append(file)

    return files


def create_file_with_extension(file: str, extension: str):
    separated = file.split(".")
    if separated[0] == "":
        return f".{''.join(separated[:-1])}.{extension}"

    return f"{''.join(separated[:-1])}.{extension}"


def dbc_to_dbf(file: str):
    dbc_file, dbf_file = [create_file_with_extension(
        file, ext) for ext in ["dbc", "dbf"]]
    result = subprocess.run(
        [BLAST] + [dbc_file, dbf_file], capture_output=True)
    logging.info(result)
    if result.returncode != 0:
        raise ChildProcessError


def dbf_to_csv(file: str):
    dbf = Dbf5(file, codec='ISO-8859-1')
    csv_file = create_file_with_extension(file, "csv")
    dbf.to_csv(csv_file)
