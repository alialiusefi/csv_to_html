from csv_to_html.src.csv.parser.csv_parser import CSVParser


def test_init():
    file_path = "fixtures/csv/test.csv"
    parser = CSVParser(file_path)
    assert parser.file_path == file_path


def test_read_all():
    file_path = "fixtures/csv/valid_csv.csv"
    parser = CSVParser(file_path)
    errors, csv_rows = parser.read_all()
    print(f"rows={csv_rows}")
    print(f"errors={errors}")
    assert len(csv_rows) == 2
