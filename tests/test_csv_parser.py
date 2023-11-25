from csv_to_pdf.csv.parser.csv_parser import CSVParser
from csv_to_pdf.csv.model.csv_classes import CSVHeaderColumn
from csv_to_pdf.csv.model.csv_classes import CSVHeader


def test_init():
    file_path = "fixtures/csv/test.csv"
    header1 = CSVHeaderColumn("column1")
    header2 = CSVHeaderColumn("column2")
    header = CSVHeader([header1, header2])

    parser = CSVParser(file_path, header)
    assert parser.file_path == file_path


def test_read_all():
    file_path = "fixtures/csv/valid_csv.csv"
    header_strings = ["Group", "Title", "Username", "Password", "URL", "Notes", "TOTP", "Icon", "Last Modified",
                      "Created"]
    header_columns = list(map(lambda x: CSVHeaderColumn(x), header_strings))
    header = CSVHeader(header_columns)
    parser = CSVParser(file_path, header)
    errors, csv_rows = parser.read_all()
    print(f"rows={csv_rows}")
    print(f"errors={errors}")
    assert len(csv_rows) == 2
