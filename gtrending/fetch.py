"""
Python library to fetch trending repositories/users using github-trending-api

Made by Hedy Li,
Code on GitHub
"""

from typing import Optional

import requests


def fetch_repos(
    language: str = "", spoken_language_code: str = "", since: str = "daily",
) -> dict:
    """Fetch trending repositories on GitHub
    
    Parameters:
        language (str, optional):  Filtering by language, eg: python
        spoken_language_code (str, optional): The spoken language, eg: en for english
        since (str, optional): The time range, choose from: [daily, weekly, monthly]. Defaults to "daily"
    
    Returns:
        A list of dicts containing information for the trending repositories found
    """
    url: str = "https://ghapi.huchen.dev/repositories?"
    url += "language=" + language
    url += "&since=" + since
    url += "&spoken_language_code=" + spoken_language_code

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
    url: str = "https://ghapi.huchen.dev/developers?"
    url += "language=" + language
    url += "&since" + since

    res = requests.get(url).json()
    return res
