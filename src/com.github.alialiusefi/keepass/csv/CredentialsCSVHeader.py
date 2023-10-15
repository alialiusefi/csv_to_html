from typing import List


class CredentialsCSVHeader:
    columns: List[str]

    def __init__(self, columns: List[str]):
        self.columns = columns
