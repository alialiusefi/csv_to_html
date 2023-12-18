import argparse

from csv_to_html.csv.parser.csv_parser import CSVParser
from csv_to_html.html.interpolator.html_interpolator import HtmlInterpolator
from csv_to_html.html.parser.html_parser import HtmlTemplateParser


def main():
    parser = argparse.ArgumentParser(
        prog='csvtohtml-cli',
        description='Parses CSV to visualize into an HTML page',
        epilog='some epilog'
    )
    parser.add_argument('convert', help='Action to convert the csv to html')
    # todo: add required flags
    parser.add_argument('--csv_file')
    parser.add_argument('--html_template_file')
    parser.add_argument('--html_output_path')
    args = parser.parse_args()

    # todo: check 'convert'
    if args.csv_file and args.html_template_file and args.html_output_path:
        csv_parser = CSVParser(args.csv_file)
        errors, csv_rows = csv_parser.read_all()
        if errors:
            print(f"Errors: ${errors}")
        html_template_parser = HtmlTemplateParser(args.html_template_file)
        html_template = html_template_parser.read_template()
        html_interpolator = HtmlInterpolator()
        html = html_interpolator.set_values(template=html_template, values=csv_rows)

        with open(args.html_output_path, 'w') as html_output_file:
            html_output_file.write(html)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
