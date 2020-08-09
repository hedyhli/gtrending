from gtrending import fetch_developers


def test_fetch_developers():
    res = fetch_developers()
    for developer in res:
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
