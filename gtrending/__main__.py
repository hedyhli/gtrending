import argparse
import pprint

from gtrending import __version__
from gtrending.fetch import fetch_developers, fetch_repos

def main():
    parser = argparse.ArgumentParser(
        prog="gtrending",
        description="Fetch trending repositories/developers on GitHub."
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )

    subparsers = parser.add_subparsers(help='sub-command help')
    parser_repo = subparsers.add_parser("repo", help="Fetch trending repositories on GitHub.")
    parser_dev = subparsers.add_parser("dev", help="Fetch trending developers on GitHub.")
    parser.add_argument("language", default="")


    args = parser.parse_args()
    if parser_repo:
        pprint.pprint(fetch_repos(args.language))
    
    if parser_dev:
        pprint.pprint(fetch_developers(args.language))
        

if __name__ == "__main__":
    main()