import re
import json


def test_langauge_list(run_cli):
    output = run_cli("langs")
    assert re.search(r"\bPython\b", output) is not None
    assert re.search(r"\bJavaScript\b", output) is not None


def test_langauge_list_json(run_cli):
    output = json.loads(run_cli("langs -j"))
    for i in output:
        assert isinstance(i, dict)
        for key in i.keys():
            assert isinstance(key, str)
            assert isinstance(i[key], str)


def test_spoken_langauge_list(run_cli):
    output = run_cli("spoken-langs")
    for line in output.strip().splitlines():
        assert re.fullmatch(r"\w\w .*", line)


def test_spoken_langauge_list_json(run_cli):
    output = json.loads(run_cli("spoken-langs -j"))
    for i in output:
        assert isinstance(i, dict)
        for key in i.keys():
            assert isinstance(key, str)
            assert isinstance(i[key], str)
