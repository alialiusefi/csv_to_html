from dataclasses import dataclass


@dataclass
class HtmlTemplate:
    set_of_place_holders: set
    html_document: str
    pass
