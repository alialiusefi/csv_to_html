from src.keepassxc_csv_to_pdf.csv.keepassxc_csv_reader import KeePassXCCSVReader


def test_init():
    file_path = "fixtures/csv/test.csv"
    reader = KeePassXCCSVReader(file_path)
    assert reader.file_path == file_path


def test_read_all():
    file_path = "fixtures/csv/test.csv"
    reader = KeePassXCCSVReader(file_path)
    list_of_rows = reader.read_all()
    print(list_of_rows)
    assert len(list_of_rows) == 2
