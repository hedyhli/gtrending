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
    url: str = "https://ghapi.huchen.dev/repositories?"
    url += "language=" + language
    url += "&since=" + since
    url += "&spoken_language_code=" + spoken_language_code

    res = requests.get(url).json()
    return res
