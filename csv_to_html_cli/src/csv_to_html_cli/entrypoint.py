import os.path

from csv_to_html.mycsv.parser.csv_parser import CSVParser
from csv_to_html.myhtml.interpolator.html_interpolator import HtmlInterpolator
from csv_to_html.myhtml.parser.html_parser import HtmlTemplateParser
import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="csvtohtml-cli",
        description="Parses CSV to visualize into an HTML page",
        epilog="some epilog",
    )
    parser.add_argument("convert", help="Action to convert the mycsv to myhtml")
    # todo: add required flags
    parser.add_argument("--csv_file")
    parser.add_argument("--html_template_file")
    parser.add_argument("--html_output_folder")
    args = parser.parse_args()

    # todo: check 'convert'
    if args.csv_file and args.html_template_file and args.html_output_folder:
        csv_parser = CSVParser(args.csv_file)
        errors, csv_rows = csv_parser.read_all()
        if errors:
            print(f"Errors: ${errors}")
        html_template_parser = HtmlTemplateParser(args.html_template_file)
        html_template = html_template_parser.read_template()
        html_interpolator = HtmlInterpolator()
        for idx, csv_row in enumerate(csv_rows):
            csv_row_values = csv_row.row_values
            map_placeholder_value = {
                csv_column_header_key.value: row_value
                for csv_column_header_key, row_value in csv_row_values.items()
            }
            html = html_interpolator.set_values(
                template=html_template,
                map_placeholder_value=map_placeholder_value,
            )
            if not os.path.isdir("test_results"):
                os.mkdir("test_results")
            with open(
                args.html_output_folder + f"/{idx}_output.html", "w+"
            ) as html_output_file:
                html_output_file.write(html)
    else:
        parser.print_help()
