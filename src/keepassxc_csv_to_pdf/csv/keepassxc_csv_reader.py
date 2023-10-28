import csv
from collections.abc import Iterator
from typing import List


class KeePassXCCSVReader:
    file_path: str
    reader: Iterator

    def __init__(self, filepath):
        self.file_path = filepath
        file = open(filepath)
        self.reader = csv.reader(file)

    def read_all(self) -> List[dict]:
        list_of_rows = []
        for row in self.reader:
            list_of_rows.append(row)
        return list_of_rows
