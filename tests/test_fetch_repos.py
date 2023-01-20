from gtrending import fetch_repos
import pytest


def test_all(repo_assertion):
    res = fetch_repos()
    repo_assertion(res)


@pytest.mark.parametrize("language", ["PYTHON", "C++", "c#", "vim-script", None])
def test_language(repo_assertion, language):
    res = fetch_repos(language=language)
    repo_assertion(res, language)


@pytest.mark.parametrize("since", ["monthly", "weekly", "daily", "", None])
def test_since(repo_assertion, since):
    res = fetch_repos(since=since)
    repo_assertion(res)


@pytest.mark.parametrize("sl", ["EN", "el", "it", "", None])
def test_spoken_language_code(repo_assertion, sl):
    res = fetch_repos(spoken_language_code=sl)
    repo_assertion(res)


@pytest.mark.parametrize("language", [0, "none", "C%2B", "Vim Script"])
def test_language_error(language):
    with pytest.raises(ValueError) as excinfo:
        fetch_repos(language)
    excinfo.match("Invalid language argument")


@pytest.mark.parametrize("since", [7, "secondly", "monthy", "annually"])
def test_since_error(since):
    with pytest.raises(ValueError) as excinfo:
        fetch_repos(since=since)
    excinfo.match("Invalid since argument")


@pytest.mark.parametrize("sl", [-1, "ENGLISH", "english", "e", " "])
def test_spoken_language_code_error(sl):
    with pytest.raises(ValueError) as excinfo:
        fetch_repos(spoken_language_code=sl)
    excinfo.match("Invalid spoken_language_code argument")
