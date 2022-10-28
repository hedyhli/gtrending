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




## Requirements
* Python 3.6 or higher


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


## API

Documentation: [Read the docs](https://gtrending.readthedocs.io/en/latest/API.html)

### `fetch_repos()`

> Fetch trending repositories on GitHub.

Parameters:
* `language (str, optional)`:  Filtering by language, eg: python
* `spoken_language_code (str, optional)`: The spoken language, eg: en for
  english
* `since (str, optional)`: The time range, choose from: [daily, weekly,
  monthly]. Defaults to "daily"

Returns:
> A list of dictionaries containing information for the trending repositories
> found.


<br>

### `fetch_developers()`

> Fetch trending developers on GitHub.

Parameters:
* `language (str, optional)`: The programming language, eg: python
* `since (str, optional)`: The time range, choose from [daily, weekly,
  monthly]. Defaults to "daily"

Returns:
> A list of dictionaries containing information for the trending developers
> found.

<br>

### `languages_list()`

> Fetch languages

Returns:
> A list of dictionaries containing programming languages.

<br>

### `spoken_languages_list()`

> Fetch spoken languages.

Returns:
> A list of spoken languages.

<br>

### `check_language()`

> Check if the language exists.

Parameters:
* `language (str)`:  The language, eg: python.

Returns:
> A boolean value. True for valid language, False otherwise.

<br>

### `check_spoken_language()`

> Check if the spoken language exists.

Parameters:
* `spoken_language_code (str)`: The spoken language, eg: English, or en, for English.

Returns:
> A boolean value. True for valid spoken language, False otherwise.

<br>

### `check_since()`

> Check if the time range is correct.

Parameters:
* `since (str)`:  The time range.

Returns:
> A boolean value. True for valid parameter, False otherwise.

---

## CLI

Usage:
```
gtrending [--json] <command> [<args>]
```

### Quick Examples

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


# Help commands
gtrending --help
# or see available arguments for specific sub-command
gtrending developers --help



## Usage with jq

# Show only fullname (user/repo) and total stars for each repo
gtrending repos --json | jq '[.[] | {fullname, stars}]'  # Still a json output

# Show only fullname for repos
gtrending repos --json | jq '.[] | .fullname'            # Not a json anymore

# Similarly for trending developers
# Show only username and repository url
gtrending developers -j | jq '[ .[] | {username, repo: .repo_url} ]'

# Show only developers with a sponsorUrl
gtrending developers -j | jq '[ map(select(.sponsorUrl != null)) | .[] | {username, repo_name: .repo.name} ]'
```



## Uses

* [github-trending-api](https://github.com/huchenme/github-trending-api) --
  JavaScript library with API
* requests -- Making API requests
