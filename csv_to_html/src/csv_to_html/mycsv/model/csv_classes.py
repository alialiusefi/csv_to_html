from dataclasses import dataclass
from typing import List, Dict


@dataclass
class CSVHeaderColumn:
    value: str

    def __hash__(self) -> int:
        return hash(self.value)

    def __eq__(self, other) -> bool:
        if type(other) is not CSVHeaderColumn:
            return False
        return self.value == other.value


@dataclass
class CSVHeader:
    list_of_columns: List[CSVHeaderColumn]
    pass

    def __init__(self, list_of_columns: List[CSVHeaderColumn]):
        self.list_of_columns = list_of_columns


@dataclass
class CSVRow:
    list_of_row_values: List[Dict[CSVHeaderColumn, str]]
