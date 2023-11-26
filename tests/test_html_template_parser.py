from csv_to_pdf.html.parser.html_parser import HtmlTemplateParser


def test_init():
    file_path = "fixtures/html/template.html"

    parser = HtmlTemplateParser(file_path)
    assert parser.file_path == file_path


def test_read_template():
    file_path = "fixtures/html/template.html"
    parser = HtmlTemplateParser(file_path)
    template = parser.read_template()
    expected = {
        "Group": "$GROUP",
        "Title": "$TITLE",
        "Username": "$USERNAME",
        "Password": "$PASSWORD"
    }
    print(template.key_value_map)
    assert template.key_value_map == expected
