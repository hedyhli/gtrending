"""Scraper"""

import re
import typing as T

import requests
from bs4 import BeautifulSoup

GHTRENDING_URL = "https://github.com/trending/"


def scrape_repos(
    quoted_language: T.Optional[str] = None,
    quoted_slc: T.Optional[str] = None,
    quoted_since: T.Optional[str] = None,
) -> T.List[dict]:
    """Scrape GitHub Trending to find repos"""

    if not quoted_language:
        quoted_language = ""
    if not quoted_slc:
        quoted_slc = ""
    if not quoted_since:
        quoted_since = "today"

    url = (
        GHTRENDING_URL + quoted_language + "?"
        f"since={quoted_since}&spoken_language_code={quoted_slc}"
    )
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    repos: T.List[dict] = []

    for article in soup.find_all("article"):
        repos.append({})
        items = [div.get_text().strip() for div in article.find_all("div")[2:]]
        items = [i.strip() for i in items[0].split("\n") if i.strip() != ""]
        # ['Rust', '601', '126', 'Built by', '189 stars today']
        try:
            items.remove("")
        except ValueError:
            pass
        try:
            items.remove("Built by")
        except ValueError:
            pass
        if len(items) == 3:
            items.insert(0, "")  # No language
        repos[-1]["language"] = items[0]
        repos[-1]["stars"] = int(items[1].replace(",", ""))
        repos[-1]["forks"] = int(items[2].replace(",", ""))
        # Remove comma separators
        repos[-1]["currentPeriodStars"] = int(
            items[-1].split(maxsplit=3)[0].replace(",", "")
        )

        full_name = [
            i.strip() for i in article.find("h2").get_text().strip().split("/")
        ]
        repos[-1]["name"] = full_name[1]
        repos[-1]["author"] = full_name[0]
        repos[-1]["avatar"] = "https://github.com/" + full_name[0] + ".png"
        repos[-1]["fullname"] = "/".join(full_name)
        repos[-1]["url"] = "https://github.com/" + "/".join(full_name)

        langcolor = article.find(class_="repo-language-color")
        repos[-1]["languageColor"] = ""
        if langcolor:
            repos[-1]["languageColor"] = "#" + langcolor["style"].split("#")[-1].strip(
                " ;"
            )

        repos[-1]["description"] = ""
        desc = article.find("p")
        if desc:
            repos[-1]["description"] = desc.get_text()

        anchors_tags = article.find_all("a")
        repos[-1]["builtBy"] = []
        for a in anchors_tags:
            anchor = a["href"]
            if anchor.startswith("/login") or anchor.startswith(f"/{full_name[0]}"):
                continue

            repos[-1]["builtBy"].append({})
            repos[-1]["builtBy"][-1]["href"] = anchor
            repos[-1]["builtBy"][-1]["username"] = anchor[1:]  # Removing leading '/'

            avatar = a.find("img", class_="avatar")
            # XXX: Better way to strip "?*" without regex? is regex faster?
            repos[-1]["builtBy"][-1]["avatar"] = ""
            if avatar:
                repos[-1]["builtBy"][-1]["avatar"] = avatar["src"].split("?")[0]

    return repos


def scrape_developers(
    quoted_language: T.Optional[str] = None,
    quoted_since: T.Optional[str] = None,
    sponsorable: T.Optional[bool] = False,
) -> T.List[dict]:
    """Scrape GitHub Trending to find developers"""

    if not quoted_language:
        quoted_language = ""
    if not quoted_since:
        quoted_since = "today"

    url = GHTRENDING_URL + "developers/" + quoted_language + "?since=" + quoted_since
    if sponsorable:
        url += "&sponsorable=1"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    devs: T.List[dict] = []
    for article in soup.find_all("article", id=re.compile("^pa-")):
        devs.append({})
        avatar = article.find("div").find("img")
        devs[-1]["avatar"] = ""
        if avatar:
            devs[-1]["avatar"] = avatar["src"].split("?")[0]
        name = article.find("h1").find("a")
        devs[-1]["name"] = name.get_text().strip()
        devs[-1]["url"] = "https://github.com" + name["href"]
        devs[-1]["username"] = name["href"][1:]

        devs[-1]["repo"] = None
        repo = article.find("article")
        if repo:
            devs[-1]["repo"] = {
                "name": "",
                "url": "",
                "description": "",
                "descriptionUrl": "",
            }
            repo_name = repo.find("h1").find("a")
            devs[-1]["repo"]["name"] = repo_name.get_text().strip()
            devs[-1]["repo"]["url"] = "https://github.com" + repo_name["href"]
            repo_desc = repo.find_all("div")[-1]
            devs[-1]["repo"]["description"] = repo_desc.get_text().strip()
            repo_desc_url = repo_desc.find("a")
            if repo_desc_url:
                devs[-1]["repo"]["descriptionUrl"] = repo_desc_url["href"]

        sponsor = article.find("a", attrs={"aria-label": re.compile("^Sponsor @")})
        devs[-1]["sponsorUrl"] = ""
        if sponsor:
            devs[-1]["sponsorUrl"] = "https://github.com" + sponsor["href"]

    return devs
