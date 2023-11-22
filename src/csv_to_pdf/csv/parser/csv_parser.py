import csv
from collections.abc import Iterator
from typing import List

from csv_to_pdf.csv.model.parsing_errors import ParsingError, MissingRowValue
from csv_to_pdf.csv.model.csv_classes import CSVRow
from csv_to_pdf.csv.model.csv_classes import CSVHeader


class CSVParser:
    file_path: str
    __reader: Iterator
    __ENCODING = "utf-8"
    __csv_header: CSVHeader

    def __init__(self, filepath, csv_header):
        self.file_path = filepath
        file = open(filepath, encoding=self.__ENCODING)
        self.__reader = csv.reader(file)
        self.__csv_header = csv_header

    def read_all(self) -> (List[ParsingError], List[CSVRow]):
        list_of_rows = []
        errors = []
        for row in self.__reader:
            row_errors, csv_row = self.read_row(row)
            if row_errors:
                row_errors.append(row_errors)
                continue
            list_of_rows.append(csv_row)
        return errors, list_of_rows

    def read_row(self, row: List[str]) -> (List[ParsingError], CSVRow):
        errors = []
        column_values = self.__csv_header.list_of_columns
        size = len(column_values)
        row_values = []
        for index in range(size):
            if size >= index:
                errors.append(MissingRowValue(column_values[index].value))
                continue
            cell = row[index]
            row_values.append({column_values[index]: cell})
        return errors, CSVRow(row_values)
