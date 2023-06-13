import pytest
import shlex
from gtrending import cli, convert_language_name_to_param


# pytest shared functions: https://stackoverflow.com/a/42156088
def repos_basic_assertions(repos, language=""):
    for repo in repos:
        print(repo)
        assert isinstance(repo["name"], str)
        assert isinstance(repo["author"], str)
        assert repo["fullname"] == f"{repo['author']}/{repo['name']}"
        assert repo["stars"] >= 0
        assert repo["forks"] >= 0
        assert repo["url"] == f"https://github.com/{repo['author']}/{repo['name']}"
        assert isinstance(repo["description"], (str, type(None)))
        assert repo["currentPeriodStars"] >= 0
        assert isinstance(repo.get("language"), (str, type(None)))
        if language and repo.get("language"):
            # Sometimes language is None even with language filtering
            assert (
                convert_language_name_to_param(repo.get("language")) == language.lower()
            )
        if "languageColor" in repo:
            if repo["languageColor"]:  # It could be None if repo language is None
                assert len(repo["languageColor"]) in [4, 7]
                assert repo["languageColor"].startswith("#")


def developers_basic_assertions(devs, sponsorable=False):
    for developer in devs:
        assert isinstance(developer["username"], str)
        assert isinstance(developer["name"], str)
        # assert developer["type"] in ("organisation", "user")
        assert developer["url"] == "https://github.com/" + developer["username"]
        assert "https://avatars" in developer["avatar"]
        assert "githubusercontent.com/u/" in developer["avatar"]
        if "repo" in str(developer.keys):
            repo = developer["repo"]
            assert isinstance(repo["name"], str)
            assert isinstance(repo["description"], str)
            assert (
                repo["url"]
                == "https://github.com/" + developer["username"] + "/" + repo["name"]
            )
        if sponsorable:
            assert developer['sponsorUrl']


@pytest.fixture
def repo_assertion():
    return repos_basic_assertions


@pytest.fixture
def developer_assertion():
    return developers_basic_assertions


@pytest.fixture
def run_cli(capsys):
    def _run_cli(command: str) -> str:
        cli.main(shlex.split(command))
        captured = capsys.readouterr()

        return captured.out

    return _run_cli
