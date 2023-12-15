from csv_to_html.html.model.html_template import HtmlTemplate
from bs4 import BeautifulSoup
import re


class HtmlInterpolator:

    def set_values(self, template: HtmlTemplate, values: dict[str, str]) -> str:
        soup = BeautifulSoup(template.html_document)
        for placeholder in template.set_of_place_holders:
            value = values[placeholder]
            soup = self.__set_value(soup, placeholder, value)
        return soup.__str__()

    def __set_value(self, soup: BeautifulSoup, placeholder: str, value: str) -> BeautifulSoup:
        element = soup.find(string=re.compile(placeholder))
        element.replace_with(value)
        return soup
