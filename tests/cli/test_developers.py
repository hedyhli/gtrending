import re
import pytest
import json


def test_json_output(run_cli, developer_assertion):
    output = json.loads(run_cli("developers -j"))

    developer_assertion(output)
    assert len(output) != 0


def test_non_json_output(run_cli):
    output = run_cli("developers")

    # https://regex101.com/r/CccCCk/4
    assert re.match(r"(^[^\s]+\n((.+)\n){2,4}\n)+", output)


@pytest.mark.parametrize("lang", ["python", "rust"])
def test_language(run_cli, developer_assertion, lang):
    output = json.loads(run_cli(f"developers -j --lang {lang}"))
    developer_assertion(output)


@pytest.mark.parametrize("since", ["daily", "weekly", "monthly"])
def test_since(run_cli, developer_assertion, since):
    output = json.loads(run_cli(f"developers -j --since {since}"))
    developer_assertion(output)


def test_sponsorable(run_cli, developer_assertion):
    output = json.loads(run_cli("developers -j --sponsorable"))
    developer_assertion(output, sponsorable=True)
