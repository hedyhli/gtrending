import pytest


def test_no_command(run_cli):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        run_cli("")
    assert pytest_wrapped_e.value.code != 0


def test_unknown_command(run_cli):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        run_cli("foo")
    assert pytest_wrapped_e.value.code != 0


def test_unknown_arg(run_cli):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        run_cli("repos --home")
    assert pytest_wrapped_e.value.code != 0


def test_unknown_arg_value(run_cli):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        run_cli("repos --since yearly")
    assert pytest_wrapped_e.value.code != 0
