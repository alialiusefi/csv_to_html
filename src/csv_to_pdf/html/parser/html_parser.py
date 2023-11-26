from bs4 import BeautifulSoup

from csv_to_pdf.html.template.template import HtmlTemplate


class HtmlTemplateParser:
    file_path: str
    __parser: BeautifulSoup | None
    pass

    def __init__(self, file_path):
        self.file_path = file_path
        self.__parser = None

    def read_template(self) -> HtmlTemplate:
        if not self.__parser:
            file = open(self.file_path)
            self.__parser = BeautifulSoup(file.read())
            file.close()
        body = self.__parser.body
        key_value_map = self.__get_key_value(body)
        return HtmlTemplate(key_value_map)

    @staticmethod
    def __get_key_value(body):
        table = body.table
        key_value_map = dict()
        for table_row in table.contents:
            if table_row == "\n":
                continue
            key = None
            value = None
            for cell in table_row.children:
                if cell == "\n" or len(cell.contents) != 1:
                    continue
                elif cell.name == "th":
                    key = cell.contents[0].strip()
                elif cell.name == "td":
                    value = cell.contents[0].strip()
                else:
                    continue
            key_value_map[key] = value
        return key_value_map


