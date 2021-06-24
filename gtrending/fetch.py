"""
Python library to fetch trending repositories/users using github-trending-api

Made by Hedy Li,
Code on GitHub
"""

from typing import Optional

import requests


def fetch_repos(
    language: str = "",
    spoken_language_code: str = "",
    since: str = "daily",
) -> dict:
    """Fetch trending repositories on GitHub

    Parameters:
        language (str, optional):  Filtering by language, eg: python
        spoken_language_code (str, optional): The spoken language, eg: en for english
        since (str, optional): The time range, choose from: [daily, weekly, monthly]. Defaults to "daily"

    Returns:
        A list of dicts containing information for the trending repositories found
    """

    if language and not check_language(language):
        raise ValueError(f"Invalid language argument: {language}")

    if spoken_language_code and not check_spoken_language(spoken_language_code):
        raise ValueError(
            f"Invalid spoken_language_code argument: {spoken_language_code}"
        )

    if since and not check_since(since):
        raise ValueError(
            f"Invalid since argument (must be 'daily', 'weekly' or 'monthly'): {since}"
        )

    url: str = f"https://gtrend.yapie.me/repositories?language={language}&since{since}&spoken_language_code={spoken_language_code}"

    res = requests.get(url).json()
    for repo in res:
        repo["fullname"] = f"{repo['author']}/{repo['name']}"
    return res


def fetch_developers(language: str = "", since: str = "daily") -> dict:
    """Fetch trending developers on GitHub

    Parameters:
        language (str, optional): The programming language, eg: python
        since (str, optional): The time range, choose from [daily, weekly, monthly]. Defaults to "daily"

    Returns:
        A list of dicts containing information for the trending developers found
    """

    if language and not check_language(language):
        raise ValueError("Language value does not exist.")

    if since and not check_since(since):
        raise ValueError("Since value is not correct.")

    url: str = f"https://gtrend.yapie.me/developers?language={language}&since{since}"

    res = requests.get(url).json()
    return res


def languages_list() -> list:
    """Fetch languages

    Returns:
        A list of dictionaries containing languages

    """
    url: str = "https://gtrend.yapie.me/languages"
    response = requests.get(url).json()
    return response


def spoken_languages_list() -> list:
    """Fetch spoken languages.

    Returns:
        A list of spoken languages
    """
    url: str = "https://gtrend.yapie.me/spoken_languages"
    response = requests.get(url).json()
    return response


def check_language(language: str = "") -> bool:
    """Check if the language exists.

    Parameters:
        language (str):  The language, eg: python.

    Returns:
        A boolean value. True for valid language, False otherwise.
    """
    languages = languages_list()
    language = language.lower()

    for name in languages:
        if language == name["name"].lower():
            return True

    return False


def check_spoken_language(spoken_language_code: str = "") -> bool:
    """Check if the spoken language exists.

    Parameters:
        spoken_language_code (str): The spoken language, eg: en for english.

    Returns:
        A boolean value. True for valid spoken language, False otherwise.
    """
    spoken_languages = spoken_languages_list()
    spoken_language_code = spoken_language_code.lower()

    for name in spoken_languages:
        if spoken_language_code == name["urlParam"].lower():
            return True

    return False


def check_since(since: str = "") -> bool:
    """Check if the time range value is correct.

    Parameters:
        since (str): The time range.

    Returns:
        A boolean value. True for valid parameter, False otherwise.
    """
    return since.lower() in ["daily", "weekly", "monthly"]
