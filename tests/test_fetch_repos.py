from gtrending import fetch_repos
import pytest



def test_all(repo_assertion):
    res = fetch_repos()
    repo_assertion(res)


def test_language(repo_assertion):
    res = fetch_repos(language="python")
    repo_assertion(res, "python")
    res = fetch_repos(language="javascript")
    repo_assertion(res, "javascript")


def test_incorrect_values():
    with pytest.raises(ValueError):
        fetch_repos("false_language")
    with pytest.raises(ValueError):
        fetch_repos("python", "false")
    with pytest.raises(ValueError):
        fetch_repos("python", "en", "annually")
