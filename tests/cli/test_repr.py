from gtrending import cli
import textwrap
import pytest

@pytest.fixture
def example_developer(): 
    return {
        "username": "alex",
        "name": "Alex Gaynor",
        "url": "https://github.com/alex",
        "sponsorUrl": None,
        "avatar": "https://avatars.githubusercontent.com/u/772",
        "repo": {
            "name": "what-happens-when",
            "description": 'An attempt ...',
            "url": "https://github.com/alex/what-happens-when",
        },
    }

def test_repr_item():
    string = cli.repr_item(
        "My Title", {"First_Key": "My First Value", "Second-Key": 42}
    )
    assert string == textwrap.dedent(
        """\
        My Title
            First_Key:  My First Value
            Second-Key: 42
        """
    )

def test_repr_repo():
    example_repo = {
        "author": "Automattic",
        "name": "pocket-casts-android",
        "avatar": "https://github.com/Automattic.png",
        "description": "Pocket Casts Android 🎧",
        "url": "https://github.com/Automattic/pocket-casts-android",
        "language": "Kotlin",
        "languageColor": "#A97BFF",
        "stars": 1495,
        "forks": 86,
        "currentPeriodStars": 246,
        "builtBy": [
            {
                "username": "ashiagr",
                "href": "https://github.com/ashiagr",
                "avatar": "https://avatars.githubusercontent.com/u/1405144",
            },
        ],
        "fullname": "Automattic/pocket-casts-android",
    }

    string = cli.repr_repo(example_repo)

    assert string == textwrap.dedent(
        """\
        pocket-casts-android
            URL:      https://github.com/Automattic/pocket-casts-android
            Author:   Automattic
            Language: Kotlin
            Forks:    86
            Stars:    1495
        """
    )

def test_repr_developer_without_sponsor(example_developer):

    string = cli.repr_developer(example_developer)
    assert string == textwrap.dedent("""\
        alex
            Name: Alex Gaynor
            URL:  https://github.com/alex
            Repo: https://github.com/alex/what-happens-when
        """)

def test_repr_developer_with_sponsor(example_developer):
    example_developer['sponsorUrl'] = 'https://sponsor'
    string = cli.repr_developer(example_developer)
    assert string == textwrap.dedent("""\
        alex
            Name:    Alex Gaynor
            URL:     https://github.com/alex
            Sponsor: https://sponsor
            Repo:    https://github.com/alex/what-happens-when
        """)

def test_repr_developer_without_repo(example_developer):
    example_developer['repo'] = None
    string = cli.repr_developer(example_developer)
    assert string == textwrap.dedent("""\
        alex
            Name: Alex Gaynor
            URL:  https://github.com/alex
        """)
