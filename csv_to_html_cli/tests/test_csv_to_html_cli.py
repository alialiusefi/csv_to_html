import os


cli_command = "csvtohtml-cli"


def test_run_help():
    exit_status = os.system('python3 ../../csv_to_html_cli/src/csv_to_html_cli/__main__.py -h')
    assert exit_status == 0
