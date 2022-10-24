from gtrending import fetch_developers
import pytest




def test_all(developer_assertion):
    res = fetch_developers()
    developer_assertion(res)


def test_language(developer_assertion):
    res = fetch_developers(language="python")
    developer_assertion(res)
    res = fetch_developers(language="javascript")
    developer_assertion(res)


def test_since(developer_assertion):
    res = fetch_developers(since="weekly")
    developer_assertion(res)
    res = fetch_developers(since="monthly")
    developer_assertion(res)


def test_incorrect_values():
    with pytest.raises(ValueError) as excinfo:
        fetch_developers("false_language")
    excinfo.match("Language value does not exist.")
    with pytest.raises(ValueError) as excinfo:
        fetch_developers("python", "annually")
    excinfo.match("Since value is not correct.")
