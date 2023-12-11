from csv_to_pdf.csv.parser.csv_parser import CSVParser
from csv_to_pdf.csv.model.csv_classes import CSVHeaderColumn
from csv_to_pdf.csv.model.csv_classes import CSVHeader


def test_init():
    file_path = "fixtures/csv/test.csv"
    header_column_1 = CSVHeaderColumn("column1")
    header_column_2 = CSVHeaderColumn("column2")
    csv_header = CSVHeader([header_column_1, header_column_2])
    parser = CSVParser(file_path, csv_header)
    assert parser.file_path == file_path


def test_read_all():
    file_path = "fixtures/csv/valid_csv.csv"
    header_columns_str = [
        "Group", "Title", "Username", "Password", "URL", "Notes", "TOTP", "Icon", "Last Modified", "Created"
    ]
    header_columns = [CSVHeaderColumn(i) for i in header_columns_str]
    header = CSVHeader(header_columns)
    parser = CSVParser(file_path, header)
    errors, csv_rows = parser.read_all()
    print(f"rows={csv_rows}")
    print(f"errors={errors}")
    assert len(csv_rows) == 2
