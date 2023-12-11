from csv_to_pdf.html.interpolator.html_interpolator import HtmlInterpolator
from csv_to_pdf.html.model.html_template import HtmlTemplate


def test_init():
    interpolator = HtmlInterpolator()
    assert interpolator is not None


def test_set_values():
    interpolator = HtmlInterpolator()
    placeholders = {"placeholder1", "placeholder2"}
    html = "<b>$placeholder2</b><h1>$placeholder1</h1>"
    template = HtmlTemplate(placeholders, html)
    values = {"placeholder1": "123", "placeholder2": "abc"}

    interpolator.set_values(template, values)

    document_with_values = template.html_document
    print(document_with_values)
    assert document_with_values.__str__() == "<b>abc</b><h1>123</h1>"
