from gtrending import fetch_developers
import pytest


def test_all(developer_assertion):
    res = fetch_developers()
    developer_assertion(res)


@pytest.mark.parametrize(
    "language", ["python", "Vim-Script", "c++", "Common-Lisp", "", None]
)
def test_language(developer_assertion, language):
    res = fetch_developers(language=language)
    developer_assertion(res)


@pytest.mark.parametrize("since", ["daily", "WEEKLY", "monthly", "", None])
def test_since(developer_assertion, since):
    res = fetch_developers(since=since)
    developer_assertion(res)


@pytest.mark.parametrize(
    "language", [tuple(), "language", "C%2B%2B", "HTML%2BDjango", "py"]
)
def test_language_error(language):
    with pytest.raises(ValueError) as excinfo:
        fetch_developers(language=language)
    excinfo.match("Invalid language argument")


@pytest.mark.parametrize("since", [[], "annually", "minutely", "daly"])
def test_since_error(since):
    with pytest.raises(ValueError) as excinfo:
        fetch_developers(since=since)
    excinfo.match("Invalid since argument")
