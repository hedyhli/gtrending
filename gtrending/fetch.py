"""
Fetch trending repositories and developers using github-trending-api
"""

from typing import List

import requests


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


def languages_list() -> list:
    """Fetch programming languages.

    Returns:
        A list of dictionaries containing languages.

    """
    url: str = "https://gtrend.yapie.me/languages"
    response = requests.get(url).json()
    return response


def spoken_languages_list() -> list:
    """Fetch spoken languages.

    Returns:
        A list of spoken languages.
    """
    url: str = "https://gtrend.yapie.me/spoken_languages"
    response = requests.get(url).json()
    return response


def check_language(language: str) -> bool:
    """Check if the language exists.

    Parameters:
        language (str):  The language, eg: python.

    Returns:
        A boolean value. True for valid language, False otherwise.
    """
    if not language:
        return False

    languages = languages_list()
    language = language.lower()

    for name in languages:
        if language == name["name"].lower():
            return True

    return False


def spoken_languages_dict() -> dict:
    sl = {}
    for entry in spoken_languages_list():
        sl[entry.get("urlParam")] = entry.get("name").split(", ")
    return sl


def spoken_languages_codes() -> list:
    """List of valid spoken language codes"""
    sl = spoken_languages_dict()
    return list(sl.keys())


def spoken_languages_names() -> list:
    """List of valid spoken language names"""
    sl = spoken_languages_dict()
    names = []
    for code in sl.keys():
        names.extend(sl[code])
    return names


def convert_spoken_language_name_to_code(sl_name: str) -> str:
    """Convert spoken language name to its code.

    Returns an empty string for invalid name.

    Parameters:
        sl_name: The spoken language name

    Returns:
        A string - the corresponding spoken_language code.
    """
    sl = spoken_languages_dict()
    for code in sl.keys():
        if sl_name in sl[code]:
            return code

    # TODO: is ValueError better?
    return ""


def check_spoken_language_name(sl: str) -> bool:
    """Check if the spoken language name exists, case-insensitive.

    Parameters:
        sl (str): The spoken language, eg: English, Spanish

    Returns:
        A boolean value. True for valid spoken language name, False otherwise.
    """
    if not sl:
        return False
    sl = sl.lower()
    return sl in [i.lower() for i in spoken_languages_names()]


def check_spoken_language_code(sl: str) -> bool:
    """Check if the spoken language code exists, case-insensitive.

    Parameters:
        sl (str): The spoken language code, eg: en, es

    Returns:
        A boolean value. True for valid spoken language code, False otherwise.
    """
    if not sl:
        return False
    sl = sl.lower()
    return sl in spoken_languages_codes()


def check_spoken_language(sl: str) -> bool:
    """Check if the spoken language code or name exists.

    Parameters:
        sl (str): The spoken language, eg: English, or en, for English.

    Returns:
        A boolean value. True for valid spoken language, False otherwise.
    """
    if not sl:
        return False
    return check_spoken_language_code(sl) or check_spoken_language_name(sl)


def check_since(since: str) -> bool:
    """Check if the time range value is correct.

    Parameters:
        since (str): The time range.

    Returns:
        A boolean value. True for valid parameter, False otherwise.
    """
    return since.lower() in ["daily", "weekly", "monthly"]
