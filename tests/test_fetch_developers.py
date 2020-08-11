from gtrending import fetch_developers


def basic_assertions(devs):
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


def test_all():
    res = fetch_developers()
    basic_assertions(res)


def test_language():
    res = fetch_developers(language="python")
    basic_assertions(res)
    res = fetch_developers(language="javascript")
    basic_assertions(res)


def test_since():
    res = fetch_developers(since="weekly")
    basic_assertions(res)
    res = fetch_developers(since="monthly")
    basic_assertions(res)
