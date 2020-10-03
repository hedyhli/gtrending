import argparse
import pprint

from gtrending import __version__
from gtrending.fetch import fetch_developers, fetch_repos


def main():
    parser = argparse.ArgumentParser(
        prog="gtrending", description="Fetch trending repositories/developers on github"
    )
    subparsers = parser.add_subparsers(help="sub-command help")

    subparser_repo = subparsers.add_parser("repo", help="Subcommand to fetch repos")
    subparser_repo.add_argument("language")

    subparser_dev = subparsers.add_parser(
        "developer", help="Subcommand to fetch developers"
    )
    subparser_dev.add_argument("language")

    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {version}".format(version=__version__),
    )
    args = parser.parse_args()

    if subparser_repo:
        repos = fetch_repos(args.language)
        pprint.pprint(repos)
    if subparser_dev:
        developers = fetch_developers(args.language)
        pprint.pprint(developers)
