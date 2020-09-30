import pytest
from gtrending import fetch_repos


def basic_assertions(repos, language=""):
    for repo in repos:
        assert isinstance(repo["name"], str)
        assert isinstance(repo["author"], str)
        assert repo["fullname"] == f"{repo['author']}/{repo['name']}"
        assert repo["stars"] >= 0
        assert repo["forks"] >= 0
        assert repo["url"] == f"https://github.com/{repo['author']}/{repo['name']}"
        assert isinstance(repo["description"], str)
        assert repo["currentPeriodStars"] >= 0
        if "language" in str(repo.keys()):
            print(repo["language"])
            assert isinstance(repo["language"], str)
        if language:
            assert repo["language"].lower() == language
        if "languageColor" in str(repo.keys()):
            assert len(repo["languageColor"]) in [4, 7]
            assert repo["languageColor"].startswith("#")


def test_all():
    res = fetch_repos()
    basic_assertions(res)


def test_language():
    res = fetch_repos(language="python")
    basic_assertions(res, "python")
    res = fetch_repos(language="javascript")
    basic_assertions(res, "javascript")


def test_incorrect_values():
    with pytest.raises(ValueError):
        fetch_repos("false_language")
    with pytest.raises(ValueError):
        fetch_repos("python", "false")
    with pytest.raises(ValueError):
        fetch_repos("python", "en", "annually")
