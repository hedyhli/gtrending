import argparse
import json

from typing import Dict

from .fetch import (
    fetch_repos,
    fetch_developers,
    languages_list,
    spoken_languages_list,
    check_language,
    check_spoken_language,
    check_since,
)


def repr_repo(repo: Dict) -> str:
    return f"""{repo['fullname']}
    Language: {repo['language']}
    Forks: {repo['forks']}"""

def main():
    arg_parser = argparse.ArgumentParser('Gtrending')
    arg_parser.add_argument('--json', '-J', action=argparse.BooleanOptionalAction, default=False)
    args = arg_parser.parse_args()
    repos = fetch_repos()
    if args.json:
        print(json.dumps(repos, indent=2))
    else:
        for repo in fetch_repos():
            print(repr_repo(repo))
