from dataclasses import dataclass


@dataclass
class ParsingError:
    pass


class EmptyValueError(ParsingError):
    field: str
    message: str
    pass

    def __init__(self, field: str):
        self.field = field
        self.message = f"{self.field} cannot be empty!"
