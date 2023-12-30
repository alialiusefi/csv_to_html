from csv_to_html.myhtml.parser.html_parser import HtmlTemplateParser


def test_init():
    file_path = "fixtures/html/template.html"

    parser = HtmlTemplateParser(file_path)
    assert parser.file_path == file_path


def test_read_template():
    file_path = "fixtures/html/template.html"
    parser = HtmlTemplateParser(file_path)
    template = parser.read_template()
    expected = {"$Group", "$Title", "$Username", "$Password"}
    print(template.set_of_place_holders)
    assert template.set_of_place_holders == expected
