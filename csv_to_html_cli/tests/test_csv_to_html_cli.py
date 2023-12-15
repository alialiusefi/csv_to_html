import os


def test_run_help():
    exit_status = os.system('csvtohtml-cli')
    assert exit_status == 0