# `gtrending`

![checks](https://github.com/hedyhli/gtrending/workflows/checks/badge.svg)
[![codecov](https://codecov.io/gh/hedyhli/gtrending/branch/master/graph/badge.svg?token=J19AQKEO4W)](https://codecov.io/gh/hedyhli/gtrending)
[![docs status](https://readthedocs.org/projects/gtrending/badge/?version=latest)](https://gtrending.readthedocs.io/en/latest/)
[![pypi version](https://img.shields.io/pypi/v/gtrending)](https://pypi.org/project/gtrending/)
[![Python Requirements](https://img.shields.io/pypi/pyversions/gtrending)](https://pypi.org/project/gtrending/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Fetch repositories and developers from [GitHub
trending](https://github.com/trending).


```python
from gtrending import fetch_repos


repos = fetch_repos(language="python")  # Returns a dictionary

for repo in repos:
    print(repo["fullname"])  # "user/repo" for each repo
```

or using the CLI

```sh
gtrending repos --language python
```

The above examples will fetch all the trending Python projects on GitHub
trending today.

[Skip to more CLI examples](#cli)


## Requirements

* Python 3.6 or higher

The only python package dependency is requests.


## Installation

gtrending is published on PyPI, use your favorite package manager and add it as
a dependency.

Pip:
```
pip3 install gtrending
```

Poetry:
```
poetry add gtrending
```

You get the idea.


## Usage

Documentation: [Read the docs (online)](https://gtrending.readthedocs.io/)

You can also download the PDF documentation build from the [latest
release](https://github.com/hedyhli/gtrending/releases) or get it from [read the
docs' dowloads](https://readthedocs.org/projects/gtrending/downloads/).


### `fetch_repos()`

Parameters:
* `language (str, optional)`:  Filtering by language, eg: python
* `spoken_language_code (str, optional)`: The spoken language, eg: en for
  english
* `since (str, optional)`: The time range, choose from: [daily, weekly,
  monthly]. Defaults to "daily"

Example:
```python-console
>>> fetch_repos(language="rust", since="weekly")
[
  {
    'author': 'iced-rs',
    'avatar': 'https://github.com/iced-rs.png',
    'builtBy': [
      {
        'avatar': 'https://avatars.githubusercontent.com/u/518289',
        'href': 'https://github.com/hecrj',
        'username': 'hecrj'
      },
      {
        'avatar': 'https://avatars.githubusercontent.com/u/10239377',
        'href': 'https://github.com/tarkah',
        'username': 'tarkah'
      },
      {
        'avatar': 'https://avatars.githubusercontent.com/u/30560559',
        'href': 'https://github.com/derezzedex',
        'username': 'derezzedex'
      },
      {
        'avatar': 'https://avatars.githubusercontent.com/u/1562417',
        'href': 'https://github.com/clarkmoody',
        'username': 'clarkmoody'
      },
      {
        'avatar': 'https://avatars.githubusercontent.com/u/4241774',
        'href': 'https://github.com/bungoboingo',
        'username': 'bungoboingo'
      }
    ],
    'currentPeriodStars': 82,
    'description': 'A cross-platform GUI library for Rust, inspired by Elm',
    'forks': 776,
    'fullname': 'iced-rs/iced',
    'language': 'Rust',
    'languageColor': '#dea584',
    'name': 'iced',
    'stars': 17647,
    'url': 'https://github.com/iced-rs/iced'
  },
  ...
]
```


### `fetch_developers()`

Parameters:
* `language (str, optional)`: The programming language, eg: python
* `since (str, optional)`: The time range, choose from [daily, weekly,
  monthly]. Defaults to "daily"

Example:
```python-console
>>> fetch_developers(language="typescript", since="weekly")
[
  {
    'avatar': 'https://avatars.githubusercontent.com/u/2230985',
    'name': 'Connor Peet',
    'repo': {
      'description': 'A resilience and transient-fault-handling library '
                     'that allows developers to express policies such as '
                     'Backoff, Retry, Circuit Breaker, Tim…',
      'name': 'cockatiel',
      'url': 'https://github.com/connor4312/cockatiel'
    },
    'sponsorUrl': None,
    'url': 'https://github.com/connor4312',
    'username': 'connor4312'
  },
  {
    'avatar': 'https://avatars.githubusercontent.com/u/13049130',
    'name': 'Robert Soriano',
    'repo': {
      'description': 'End-to-end typesafe APIs in Nuxt applications.',
      'name': 'trpc-nuxt',
      'url': 'https://github.com/wobsoriano/trpc-nuxt'
    },
    'sponsorUrl': None,
    'url': 'https://github.com/wobsoriano',
    'username': 'wobsoriano'
  },
  ...
]
```

<br>

### `languages_list()`

A list of dictionaries with each name to its parameter value:

```python-console
>>> languages_list()
[
  ...
  {
    "name": "Elm",
    "param": "elm"
  },
  {
    "name": "Emacs Lisp",
    "param": "emacs-lisp"
  },
  {
    "name": "EmberScript",
    "param": "emberscript"
  },
  {
    "name": "EQ",
    "param": "eq"
  },
  ...
]
```

<br>

### `spoken_languages_list()`

```python-console
>>> spoken_languages_list()
[
  ...
  {
    "code": "it"
    "name": [ "Italian" ],
  },
  {
    "code": "iu"
    "name": [ "Inuktitut" ],
  },
  {
    "code": "ja"
    "name": [ "Japanese" ],
  },
  {
    "code": "jv"
    "name": [ "Javanese" ],
  },
  {
    "code": "kl"
    "name": [ "Kalaallisut", "Greenlandic" ],
  },
  ...
]
```

<br>

### `check_language()`

Validate the language parameter:

```python-console
>>> check_language("python")
True
>>> check_language("Ruby")
True
>>> check_language("TeaScript")  # Does not exist
False
>>> check_language("")
False
```

<br>

### `check_spoken_language_code()`

Validate the spoken language code parameter:

```python-console
>>> check_spoken_language_code("es")
True
>>> check_spoken_language_code("FR")
True
>>> check_spoken_language_code("ZZ")  # Does not exist
False
>>> check_spoken_language_code("")
False
```

<br>

### `check_since()`

Check if the time range is correct — it must be daily, weekly, or monthly —
case-insensitive.

---

For more API usage details, go read the docs!

---

## CLI

Usage:
```
gtrending [--json] <command> [<args>]
```

### Examples

```sh
# Sort repos by stars
gtrending repos --sort stars

# See only python repositories
gtrending repos --language python

# See weekly trending repos
gtrending repos --since weekly --sort forks

# Print output in json format (-j/--json)
gtrending repos --json

# See trending rust developers
gtrending developers --language rust

# See available coding languages
gtrending langs

# See available spoken languages
gtrending spoken-langs
```

**Getting help**
```sh
# Help commands
gtrending --help
# or see available arguments for specific sub-command
gtrending developers --help
```

**Usage with jq**
```sh
# Show only fullname (user/repo) and total stars for each repo
# Still a json output
gtrending repos --json | jq '[.[] | {fullname, stars}]'

# Show only fullname for repos
# Not a json anymore
gtrending repos --json | jq '.[] | .fullname'

# Similarly for trending developers
# Show only username and repository url
gtrending developers -j | jq '[ .[] | {username, repo: .repo_url} ]'

# Show only developers with a sponsorUrl
gtrending developers -j | jq '[ map(select(.sponsorUrl != null)) | .[] | {username, repo_name: .repo.name} ]'
```

## Uses

* [github-trending-api](https://github.com/huchenme/github-trending-api) —
  JavaScript library with web API
* requests — Making API requests
