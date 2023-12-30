import os

main = "../../csv_to_html_cli/src/csv_to_html_cli/__main__.py"


def test_run_help():
    command = f"python3 {main} -h"
    exit_status = os.system(command)
    assert exit_status == 0


def test_convert_csv_to_html():
    csv_file_path = "./fixtures/valid_csv.csv"
    html_template_file = "./fixtures/template.html"
    html_output_path = "/test_results/output.html"
    command = (f"python3 {main} convert "
               f"--csv_file {csv_file_path} "
               f"--html_template_file {html_template_file} "
               f"--html_output_path {html_output_path}")

    exit_status = os.system(command)
    assert exit_status == 0
