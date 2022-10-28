import os


def test_named_execution():
    exit_code = os.system("gtrending --help")
    assert exit_code == 0


def test_module_execution():
    exit_code = os.system("python -m gtrending --help")
    assert exit_code == 0
