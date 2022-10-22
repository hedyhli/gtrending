import argparse
import json

from typing import Dict, Any

from .fetch import (
    fetch_repos,
    fetch_developers,
    languages_list,
    spoken_languages_list,
    check_language,
    check_spoken_language,
    check_since,
)
"""
gtrending repos
gtrending devs|developers
gtrending lang|code-lang
gtrending spoken-lang

"""

def print_json(value):
    print(json.dumps(value, indent=2))

def _repr_item(title: str, props: Dict[str, Any]) -> str:
    string = title + '\n'
    indent = " "*4 
    max_key_len = len(max(props.keys(), key=len))
    for key, value in props.items():
        string += indent + (key + ':').ljust(max_key_len+2) + str(value) + "\n"
    return string
    

def repr_repo(repo: Dict) -> str:
    title = repo['name']
    props = {
        'URL': repo['url'],
        'Author': repo['author'],
        'Language': repo['language'],
        'Forks': repo['forks'],
        'Stars': repo['stars'],
    }
    return _repr_item(title, props)


def repr_developer(developer: Dict) -> str:
    title = developer['username']
    props = {
        'Name': developer['name'],
        'URL': developer['url']
    }

    if developer['sponsorUrl'] is not None:
        props['Sponsor'] = developer['sponsorUrl']

    if developer['repo'] is not None:
        props['Repo'] = developer['repo']['url']

    return _repr_item(title, props)


def show_repos(args: argparse.Namespace):
    repos = fetch_repos(
        language=args.language,
        spoken_language_code=args.spoken_language,
        since=args.since
    )

    repos.sort(
        key=lambda repo: repo.get(args.sort),
        reverse=args.sort_reverse
    )

    if args.json:
        print_json(repos)
    else:
        for repo in repos:
            print(repr_repo(repo))


def show_developers(args: argparse.Namespace):
    developers = fetch_developers(
        language=args.language,
        since=args.since
    )

    developers.sort(key = lambda dev: dev['username'])

    if args.json:
        print_json(developers)
    else:
        for dev in developers:
            print(repr_developer(dev))


def show_langs(args: argparse.Namespace):
    langauges = languages_list()

    if args.json:
        print_json(langauges)
    else:
        for entry in languages_list():
            print(entry["name"])


def show_spoken_langs(args: argparse.Namespace):
    spoken_languages = spoken_languages_list()

    if args.json:
        print_json(spoken_languages)
    else:
        for entry in spoken_languages_list():
            print(entry["urlParam"], entry["name"])


def main():
    json_parser = argparse.ArgumentParser(add_help=False)
    json_parser.add_argument(
        '--json',
        '-J',
        action=argparse.BooleanOptionalAction,
        default=False,
    )

    parser = argparse.ArgumentParser('Gtrending')
    subparser = parser.add_subparsers(dest='command')
  

    parser_repo = subparser.add_parser(
        'repos',
        parents=[json_parser]
    )
    parser_repo.add_argument(
        '--language',
        '--lang',
        '-L',
        default=""
    )
    parser_repo.add_argument(
        '--spoken-language',
        '--spoken-lang',
        default=""
    )
    parser_repo.add_argument('--since', type=str, choices=['daily', 'monthly', 'weekly'], default='daily')
    parser_repo.add_argument('--sort', type=str, choices=['name', 'forks', 'stars'], default='name')
    parser_repo.add_argument('--sort-reverse', type=bool, action=argparse.BooleanOptionalAction, default=False)
    parser_repo.set_defaults(func=show_repos)

    # Developer command
    parser_developer = subparser.add_parser(
        'developers',
        parents=[json_parser]
    )
    parser_developer.add_argument(
        '--language',
        '--lang',
        '-L',
        default=""
    )
    parser_developer.add_argument(
        '--since',
        type=str,
        choices=['daily', 'monthly', 'weekly'],
        default='daily'
    )
    parser_developer.set_defaults(func=show_developers)

    parser_developer = subparser.add_parser('langs', parents=[json_parser])
    parser_developer.set_defaults(func=show_langs)

    parser_developer = subparser.add_parser('spoken-langs', parents=[json_parser])
    parser_developer.set_defaults(func=show_spoken_langs)

    args = parser.parse_args()
    if args.command == None:
        parser.print_help()
        exit(1)
    else:
        args.func(args)
