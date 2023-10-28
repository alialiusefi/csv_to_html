from keepassxc_csv_to_pdf.csv.KeePassXCCSVReader import KeePassXCCSVReader


def test_init():
    file_path = "filepath.csv"
    reader = KeePassXCCSVReader(file_path)
    assert reader.file_path == file_path
