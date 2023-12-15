import os


def test_run_help():
    exit_status = os.system('csv_to_html_cli')
    assert exit_status == 0