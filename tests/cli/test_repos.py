import pytest
import re
import json


def test_json_output(run_cli, repo_assertion):
    output = json.loads(run_cli("repos -j"))

    assert len(output) != 0
    repo_assertion(output)


def test_non_json_output(run_cli):
    output = run_cli("repos")

    # https://regex101.com/r/CccCCk/4
    assert re.match(r"(^[^\s]+\n((.+)\n){5}\n)+", output)


@pytest.mark.parametrize("lang", ["python", "rust"])
def test_language(run_cli, repo_assertion, lang):
    output = json.loads(run_cli(f"repos --lang {lang} -j"))
    repo_assertion(output, lang)


@pytest.mark.parametrize("sort_key", ["name", "forks", "stars"])
def test_sorting(sort_key, run_cli, repo_assertion):
    output = json.loads(run_cli(f"repos --sort {sort_key} -j"))
    repo_assertion(output)

    assert output == sorted(output, key=lambda repo: repo[sort_key])
