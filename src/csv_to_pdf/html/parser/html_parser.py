from bs4 import BeautifulSoup

from csv_to_pdf.html.model.template import HtmlTemplate


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
        set_of_place_holders = self.__get_placeholder(body)
        return HtmlTemplate(set_of_place_holders, body)

    @staticmethod
    def __get_placeholder(body):
        table = body.table
        set_of_placeholders = set()
        for table_row in table.contents:
            if table_row == "\n":
                continue
            for cell in table_row.children:
                if cell.name == "td" and len(cell.contents) == 1:
                    placeholder = cell.contents[0].strip()
                    set_of_placeholders.add(placeholder)
        return set_of_placeholders
