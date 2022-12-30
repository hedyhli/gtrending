import re
import json


def test_langauge_list(run_cli):
    output = run_cli("langs")
    assert re.search(r"\bpython\b", output) is not None
    assert re.search(r"\bhtml\+django\b", output) is not None


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
        assert re.fullmatch(r"\w\w", line)


def test_spoken_langauge_list_json(run_cli):
    output = json.loads(run_cli("spoken-langs -j"))
    for i in output:
        assert isinstance(i, dict)
        assert len(i.keys()) == 2
        assert "code" in i.keys()
        assert "name" in i.keys()
        assert isinstance(i["code"], str)
        assert isinstance(i["name"], list)
        assert i["name"]
        for name in i["name"]:
            assert isinstance(name, str)
            assert not name.islower()
