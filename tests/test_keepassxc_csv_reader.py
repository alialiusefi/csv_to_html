from csv_to_pdf.csv.reader.csv_reader import CSVReader


def test_init():
    file_path = "fixtures/csv/test.csv"
    reader = CSVReader(file_path)
    assert reader.file_path == file_path


def test_read_all():
    file_path = "fixtures/csv/test.csv"
    reader = CSVReader(file_path)
    list_of_rows = reader.read_all()
    print(list_of_rows)
    assert len(list_of_rows) == 2
