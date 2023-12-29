import csv as pycsv
from collections.abc import Iterator
from typing import List

from ..model.parsing_errors import ParsingError
from ..model.csv_classes import CSVRow, CSVHeaderColumn
from ..model.csv_classes import CSVHeader


class CSVParser:
    file_path: str
    __reader: Iterator
    __ENCODING = "utf-8"
    __csv_header: CSVHeader

    def __init__(self, filepath):
        self.file_path = filepath
        file = open(filepath, encoding=self.__ENCODING)
        self.__reader = pycsv.reader(file)
        header_strings = next(self.__reader)
        self.__csv_header = CSVHeader([CSVHeaderColumn(i) for i in header_strings])

    def read_all(self) -> (List[ParsingError], List[CSVRow]):
        list_of_rows = []
        errors = []
        for row in self.__reader:
            row_errors, csv_row = self.read_row(row)
            if row_errors:
                errors.append(row_errors)
            else:
                list_of_rows.append(csv_row)
        return errors, list_of_rows

    def read_row(self, row: List[str]) -> (List[ParsingError], CSVRow):
        errors = []
        row_values = []
        column_values = self.__csv_header.list_of_columns
        header_column_size = len(column_values)
        row_size = len(row)
        if row_size < header_column_size:
            return [], []
        for index in range(header_column_size):
            cell = row[index]
            header_value = column_values[index].value
            row_values.append({header_value: cell})
        return errors, CSVRow(row_values)
