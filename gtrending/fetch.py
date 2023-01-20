"""
Fetch trending repositories and developers using github-trending-api
"""

from urllib.parse import quote as urlquote
from typing import List, Optional

import requests

from .paramutils import (
    check_language,
    check_spoken_language_code,
    check_since,
    convert_language_name_to_param,
)


def fetch_repos(
    language: Optional[str] = "",
    spoken_language_code: Optional[str] = "",
    since: Optional[str] = "daily",
) -> List[dict]:
    """Fetch trending repositories on GitHub.

    Parameters:
        language (str, optional):  Filtering by language, eg: python, common-lisp
        spoken_language_code (str, optional): The spoken language, eg: en for english
        since (str, optional): The time range, choose from: [daily, weekly, monthly].
        Defaults to "daily".

    Note:
        spoken_language_code argument must be the language code ("en" and not
        "english"). To convert language name to language code, use
        convert_spoken_language_name_to_code().

        Likewise, language argument must be the parameter value ("common-lisp"
        not "Common Lisp"). To convert the name to param, use
        convert_language_name_to_param().

    Returns:
        list(dict): A list of dictionaries containing information for each trending repository found

    Raises:
        ValueError: When any of the arguments are invalid

    Examples:
        ::

            fetch_repos()
            fetch_repos(language="python")
            fetch_repos("C", "zh", "monthly")
    """

    # or has lower precedence than and
    if (
        not isinstance(language, (str, type(None)))
        or language
        and not check_language(language)
    ):
        raise ValueError(f"Invalid language argument: {language}")
    language_param = urlquote(language, safe="+") if language else ""

    if (
        not isinstance(spoken_language_code, (str, type(None)))
        or spoken_language_code
        and not check_spoken_language_code(spoken_language_code)
    ):
        raise ValueError(
            f"Invalid spoken_language_code argument: {spoken_language_code}"
        )

    if not isinstance(since, (str, type(None))) or since and not check_since(since):
        raise ValueError(
            f"Invalid since argument (must be 'daily', 'weekly' or 'monthly'): {since}"
        )
    since = since or "daily"

    url: str = (
        "https://gtrend.yapie.me/repositories?"
        f"language={language_param}&since={since}&spoken_language_code={spoken_language_code}"
    )

    res = requests.get(url).json()
    repos = []
    for repo in res:
        repo["fullname"] = f"{repo['author']}/{repo['name']}"
        repo_language = repo.get("language")
        # Edge cases
        if language:
            if (
                not repo_language
                or convert_language_name_to_param(repo_language).lower()
                != language.lower()
            ):
                continue  # pragma: no cover
        if not repo.get("forks"):  # Sometimes forks is None
            repo["forks"] = 0  # pragma: no cover
        if not repo.get("stars"):
            repo["stars"] = 0  # pragma: no cover
        if not repo.get("currentPeriodStars"):
            repo["currentPeriodStars"] = 0  # pragma: no cover

        repos.append(repo)
    return repos


def fetch_developers(
    language: Optional[str] = "", since: Optional[str] = "daily"
) -> List[dict]:
    """Fetch trending developers on GitHub.

    Parameters:
        language (str, optional): The programming language, eg: python
        since (str, optional): The time range, choose from [daily, weekly, monthly].
        Defaults to "daily".

    Returns:
        list(dict): A list of dictionaries containing information for each trending developer found

    Raises:
        ValueError: When any of the arguments are invalid

    Examples:
        ::

            fetch_developers()
            fetch_repos(language="python")
            fetch_repos("C", since="monthly")
    """

    if (
        not isinstance(language, (str, type(None)))
        or language
        and not check_language(language)
    ):
        raise ValueError(f"Invalid language argument: {language}")
    language_param = urlquote(language, safe="+") if language else ""

    if not isinstance(since, (str, type(None))) or since and not check_since(since):
        raise ValueError(
            f"Invalid since argument (must be 'daily', 'weekly' or 'monthly'): {since}"
        )

    url: str = (
        f"https://gtrend.yapie.me/developers?language={language_param}&since={since}"
    )

    res = requests.get(url).json()
    return res
