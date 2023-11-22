from typing import List

from csv_to_pdf.csv.model.parsing_errors import (
    IncorrectHeaderError,
    ParsingError,
    EmptyValueError,
)


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

    def __append_if_true(
        self,
        boolean: bool,
        error: ParsingError,
        list_of_errors: List[ParsingError],
    ):
        if boolean:
            list_of_errors += error

    def __validate_empty(self, row: List[str], errors: List[ParsingError]):
        self.__append_if_true(
            row[1].strip() == "", EmptyValueError(self.__header[1]), errors
        )
        self.__append_if_true(
            row[2].strip() == "", EmptyValueError(self.__header[2]), errors
        )
        self.__append_if_true(
            row[2].strip() == "", EmptyValueError(self.__header[2]), errors
        )
