"""
Fetch trending repositories and developers using github-trending-api
"""

from urllib.parse import quote as urlquote
from typing import List

import requests

from .paramutils import (
    check_language,
    spoken_languages_dict,
    spoken_languages_codes,
    spoken_languages_names,
    convert_spoken_language_name_to_code,
    convert_language_name_to_param,
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

    Parameters:
        language (str, optional):  Filtering by language, eg: python, common-lisp
        spoken_language_code (str, optional): The spoken language, eg: en for english
        since (str, optional): The time range, choose from: [daily, weekly, monthly]. Defaults to "daily"

    Note:
        spoken_language_code argument must be the language code ("en" and not
        "english"). To convert language name to language code, use
        convert_spoken_language_name_to_code().

        Likewise, language argument must be the parameter value ("common-lisp"
        not "Common Lisp"). To convert the name to param, use
        convert_language_name_to_param()


    Returns:
        A list of dictionary containing information for the trending repositories found.
    """

    # or has lower precedence than and
    if not isinstance(language, str) or language and not check_language(language):
        raise ValueError(f"Invalid language argument: {language}")
    language_param = urlquote(language)

    if not isinstance(spoken_language_code, str) or spoken_language_code and not check_spoken_language_code(spoken_language_code):
        raise ValueError(
            f"Invalid spoken_language_code argument: {spoken_language_code}"
        )

    if not isinstance(since, str) or since and not check_since(since):
        raise ValueError(
            f"Invalid since argument (must be 'daily', 'weekly' or 'monthly'): {since}"
        )
    since = since or "daily"

    url: str = f"https://gtrend.yapie.me/repositories?language={language_param}&since={since}&spoken_language_code={spoken_language_code}"

    res = requests.get(url).json()
    repos = []
    for repo in res:
        repo["fullname"] = f"{repo['author']}/{repo['name']}"
        repo_language = repo.get("language")
        # Edge cases
        if language:
            if not repo_language or convert_language_name_to_param(repo_language).lower() != language.lower():
                continue  # pragma: no cover
        if not repo.get("forks"):  # Sometimes forks is None
            repo["forks"] = 0  # pragma: no cover
        if not repo.get("stars"):
            repo["stars"] = 0  # pragma: no cover

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

    if not isinstance(language, str) or language and not check_language(language):
        raise ValueError(f"Invalid language argument: {language}")
    language_param = urlquote(language, safe="+")

    if not isinstance(since, str) or since and not check_since(since):
        raise ValueError(
            f"Invalid since argument (must be 'daily', 'weekly' or 'monthly'): {since}"
        )

    url: str = f"https://gtrend.yapie.me/developers?language={language_param}&since={since}"

    res = requests.get(url).json()
    return res
