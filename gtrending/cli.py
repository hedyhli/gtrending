"""Gtrending CLI module"""

import argparse
import json

from typing import Dict, Any

from .fetch import (
    fetch_repos,
    fetch_developers,
)
from .paramutils import (
    languages_list,
    spoken_languages_list,
)


def main(args=None):
    parser = argparse.ArgumentParser(
        "gtrending",
        description="Query the GitHub Trending page",
        usage="gtrending [--json] <command> [<args>]",
        epilog="Run `gtrending <command> --help` for more details",
    )

    # This is a workaround to allow `--json` to be used before command names
    # like `gtrending --json repos` and to keep `--json` in the main help message
    parser.add_argument(
        "-j",
        "--json",
        help="Print output in json format",
        action="store_true",
        default=False,
        dest="json_main",  # see: https://stackoverflow.com/a/37933841
    )

    subparser = parser.add_subparsers(
        title="commands", dest="command", prog="gtrending"
    )

    # Extract common arguments in parents
    parent_json = argparse.ArgumentParser(add_help=False)
    parent_json.add_argument(
        "-j",
        "--json",
        dest="json",
        help="Print output in json format",
        action="store_true",
        default=False,
    )

    parent_filter = argparse.ArgumentParser(add_help=False)
    parent_filter.add_argument(
        "-l",
        "--language",
        dest="language",
        metavar="lang",
        help="One of the supported coding languages",
        default="",
    )
    parent_filter.add_argument(
        "-s",
        "--since",
        dest="since",
        type=str,
        metavar="duration",
        help="Options: 'daily', 'monthly' or 'weekly'",
        choices=["daily", "monthly", "weekly"],
        default="daily",
    )

    parser_repo = subparser.add_parser(
        "repos", help="Fetch trending repos", parents=[parent_json, parent_filter]
    )
    parser_repo.add_argument(
        "-S",
        "--spoken-language",
        dest="spoken_language",
        help="One of the supported spoken languages",
        metavar="spoken_lang",
        default="",
    )
    parser_repo.add_argument(
        "--sort",
        metavar="key",
        help="Options: 'name', 'forks' and 'stars'",
        type=str,
        choices=["name", "forks", "stars"],
        default="name",
    )
    parser_repo.add_argument(
        "-r", "--sort-reverse", dest="sort_reverse", action="store_true", default=False
    )
    parser_repo.set_defaults(func=show_repos)

    parser_developer = subparser.add_parser(
        "developers",
        help="Fetch trending developers",
        parents=[parent_json, parent_filter],
    )
    parser_developer.set_defaults(func=show_developers)

    parser_langs = subparser.add_parser(
        "langs", help="Fetch list of supported coding languages", parents=[parent_json]
    )
    parser_langs.set_defaults(func=show_langs)

    parser_spoken_langs = subparser.add_parser(
        "spoken-langs",
        help="Fetch list of supported spoken languages",
        parents=[parent_json],
    )
    parser_spoken_langs.set_defaults(func=show_spoken_langs)

    args = parser.parse_args(args)
    if args.command == None:
        parser.print_help()
        exit(1)
    else:
        args.json = args.json or args.json_main
        args.func(args)


def show_developers(args: argparse.Namespace):
    developers = fetch_developers(language=args.language, since=args.since)

    developers.sort(key=lambda dev: dev["username"])

    if args.json:
        print_json(developers)
    else:
        for dev in developers:
            print(repr_developer(dev))


def show_langs(args: argparse.Namespace):
    languages = languages_list()

    if args.json:
        print_json(languages)
    else:
        for entry in languages_list():
            print(entry["param"])


def show_spoken_langs(args: argparse.Namespace):
    spoken_languages = spoken_languages_list()

    if args.json:
        print_json(spoken_languages)
    else:
        for entry in spoken_languages_list():
            print(entry["code"])


def show_repos(args: argparse.Namespace):
    repos = fetch_repos(
        language=args.language,
        spoken_language_code=args.spoken_language,
        since=args.since,
    )

    repos.sort(key=lambda repo: repo[args.sort], reverse=args.sort_reverse)

    if args.json:
        print_json(repos)
    else:
        for repo in repos:
            print(repr_repo(repo))


def repr_repo(repo: Dict) -> str:
    title = repo["name"]
    props = {
        "URL": repo["url"],
        "Author": repo["author"],
        "Language": repo["language"],
        "Forks": repo["forks"],
        "Stars": repo["stars"],
    }
    return repr_item(title, props)


def repr_developer(developer: Dict) -> str:
    title = developer["username"]
    props = {"Name": developer["name"], "URL": developer["url"]}

    if developer["sponsorUrl"] is not None:
        props["Sponsor"] = developer["sponsorUrl"]

    if developer["repo"] is not None:
        props["Repo"] = developer["repo"]["url"]

    return repr_item(title, props)


def repr_item(title: str, props: Dict[str, Any]) -> str:
    string = title + "\n"
    indent = " " * 4
    max_key_len = len(max(props.keys(), key=len))
    for key, value in props.items():
        string += indent + (key + ":").ljust(max_key_len + 2) + str(value) + "\n"
    return string


def print_json(value):
    print(json.dumps(value, indent=2))
