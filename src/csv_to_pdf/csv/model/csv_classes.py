from dataclasses import dataclass
from typing import List, Dict


@dataclass
class CSVHeaderColumn:
    value: str


@dataclass
class CSVHeader:
    list_of_columns: List[CSVHeaderColumn]


@dataclass
class CSVRow:
    list_of_row_values: List[Dict[CSVHeaderColumn, str]]
