from gtrending import fetch_repos


def test_fetch_repos():
    res = fetch_repos()
    for repo in res:
        assert isinstance(repo["name"], str)
        assert isinstance(repo["author"], str)
        assert repo["stars"] >= 0
        assert repo["forks"] >= 0
        assert repo["url"] == f"https://github.com/{repo['author']}/{repo['name']}"
        assert isinstance(repo["description"], str)
        assert repo["currentPeriodStars"] >= 0
