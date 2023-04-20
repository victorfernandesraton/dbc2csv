from logging import Logger
from dbc2csv.utils import dbc_to_dbf, dbf_to_csv, discover_files


class Dbc2bfc:
    def __init__(self, log: Logger) -> None:
        self.log = log

    def run(self, dir: str):
        dbc_files = discover_files(dir, "dbc")
        total_dbc = len(dbc_files)
        self.log.info(f"{total_dbc} .dbc file to be proccess")

        for file in dbc_files:
            self.log.info(file)
            dbc_to_dbf(file)

        dbf_files = discover_files(dir, "dbf")
        total_dbf = len(dbf_files)
        self.log.info(f"{total_dbf} .dbf file to be proccess")

        for file in dbf_files:
            self.log.info(file)
            dbf_to_csv(file)

        csv_files = discover_files(dir, "csv")
        total_conversion = len(csv_files)

        self.log.info(f"{total_conversion} .csv file to be proccess")
