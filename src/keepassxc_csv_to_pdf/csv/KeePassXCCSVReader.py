import csv
from typing import List


class KeePassXCCSVReader:
    file_path: str

    def __init__(self, filepath):
        self.file_path = filepath

    # def hasNext(self, rows = 1) -> bool:
    #
    # def getNext(self, rows = 1) -> List[dict]:

