import csv
from collections.abc import Iterator
from typing import List

from csv_to_pdf.csv.model.parsing_errors import ParsingError
from csv_to_pdf.csv.model.keepassxc_csv_row import KeePassXCCSVRow


class CSVReader:
    file_path: str
    __reader: Iterator
    __ENCODING = "utf-8"

    def __init__(self, filepath):
        self.file_path = filepath
        file = open(filepath, encoding="utf-8")
        self.__reader = csv.reader(file)

    def read_all(self) -> (List[ParsingError], List[KeePassXCCSVRow]):
        list_of_rows = []
        for row in self.__reader:
            list_of_rows.append(row)
        return list_of_rows

    def read_row(self, row) -> (List[ParsingError], KeePassXCCSVRow):
        obj = KeePassXCCSVRow(
            group=row[0],
            title=row[1],
            username=row[2],
            password=row[3],
            url=row[4],
            notes=row[5],
            totp=row[6],
            icon=row[7],
            last_modified=row[8],
            created=row[9],
        )
        return obj
