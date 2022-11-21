"""
Fetch trending repositories and developers using github-trending-api
"""

from typing import List

import requests

from .paramutils import (
    check_language,
    spoken_languages_dict,
    spoken_languages_codes,
    spoken_languages_names,
    convert_spoken_language_name_to_code,
    check_spoken_language_name,
    check_spoken_language_code,
    check_spoken_language,
    check_since,
)


def fetch_repos(
    language: str = "",
    spoken_language_code: str = "",
    since: str = "daily",
) -> List[dict]:
    """Fetch trending repositories on GitHub.

    Note: spoken_language_code argument must be the language code ("en" and not
    "english"). To convert language name to language code, use
    convert_spoken_language_name_to_code()

    Parameters:
        language (str, optional):  Filtering by language, eg: python
        spoken_language_code (str, optional): The spoken language, eg: en for english
        since (str, optional): The time range, choose from: [daily, weekly, monthly]. Defaults to "daily"

    Returns:
        A list of dictionary containing information for the trending repositories found.
    """

    if language and not check_language(language):
        raise ValueError(f"Invalid language argument: {language}")

    if spoken_language_code and not check_spoken_language_code(spoken_language_code):
        raise ValueError(
            f"Invalid spoken_language_code argument: {spoken_language_code}"
        )

    if since and not check_since(since):
        raise ValueError(
            f"Invalid since argument (must be 'daily', 'weekly' or 'monthly'): {since}"
        )

    url: str = f"https://gtrend.yapie.me/repositories?language={language}&since={since}&spoken_language_code={spoken_language_code}"

    res = requests.get(url).json()
    repos = []
    for repo in res:
        repo["fullname"] = f"{repo['author']}/{repo['name']}"
        repo_language = repo.get("language")
        if language:
            if not repo_language or repo_language.lower() != language.lower():
                continue  # pragma: no cover
        repos.append(repo)
    return repos


def fetch_developers(language: str = "", since: str = "daily") -> List[dict]:
    """Fetch trending developers on GitHub.

    Parameters:
        language (str, optional): The programming language, eg: python
        since (str, optional): The time range, choose from [daily, weekly, monthly]. Defaults to "daily"

    Returns:
        A list of dictionary containing information for the trending developers found.
    """

    if language and not check_language(language):
        raise ValueError("Language value does not exist.")

    if since and not check_since(since):
        raise ValueError("Since value is not correct.")

    url: str = f"https://gtrend.yapie.me/developers?language={language}&since={since}"

    res = requests.get(url).json()
    return res
