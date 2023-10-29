from typing import List

from keepassxc_csv_to_pdf.csv.model.parsing_errors import IncorrectHeaderError


class KeePassXCCSVValidator:
    __header = [
        "Group",
        "Title",
        "Username",
        "Password",
        "URL",
        "Notes",
        "TOTP",
        "Icon",
        "Last Modified",
        "Created",
    ]

    def __validate_header(self, header_row: List[str]) -> IncorrectHeaderError:
        if header_row != self.__header:
            return IncorrectHeaderError()
