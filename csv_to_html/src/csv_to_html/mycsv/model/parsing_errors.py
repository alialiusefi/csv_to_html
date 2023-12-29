from dataclasses import dataclass


@dataclass
class ParsingError:
    message: str
    pass


@dataclass
class EmptyValueError(ParsingError):
    field: str
    pass

    def __init__(self, field: str):
        self.field = field
        self.message = f"{self.field} cannot be empty!"


@dataclass
class MissingRowValue(ParsingError):
    message: str
    pass

    def __init__(self, field: str):
        self.field = field
        self.message = f"{self.field} is missing!"


@dataclass
class IncorrectHeaderError(ParsingError):
    def __init__(self):
        self.message = "Incorrect header format."
