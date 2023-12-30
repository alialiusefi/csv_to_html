from typing import Dict

from ..model.html_template import HtmlTemplate
from bs4 import BeautifulSoup
import re


class HtmlInterpolator:
    def set_values(
        self, template: HtmlTemplate, map_placeholder_value: Dict[str, str]
    ) -> str:
        str_template = template.html_document.__str__()
        soup = BeautifulSoup(str_template)
        for placeholder in template.set_of_place_holders:
            value = map_placeholder_value.get(placeholder, None)
            if value:
                soup = self.__set_value(soup, placeholder, value)
        return soup.__str__()

    def __set_value(
        self, soup: BeautifulSoup, placeholder: str, value: str
    ) -> BeautifulSoup:
        escaped_placeholder = placeholder.replace("$", "\\$")
        element = soup.find(string=re.compile(escaped_placeholder))
        element.replace_with(value)
        return soup
