# `gtrending`

![checks](https://github.com/hedythedev/gtrending/workflows/checks/badge.svg)
[![codecov](https://codecov.io/gh/hedythedev/gtrending/branch/master/graph/badge.svg?token=J19AQKEO4W)](https://codecov.io/gh/hedythedev/gtrending)
[![docs status](https://readthedocs.org/projects/gtrending/badge/?version=latest)](https://gtrending.readthedocs.io/en/latest/)
[![pypi version](https://img.shields.io/pypi/v/gtrending)](https://pypi.org/project/gtrending/)
[![Python Requirements](https://img.shields.io/pypi/pyversions/gtrending)](https://pypi.org/project/gtrending/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Lightweight and easy-to-use python library for fetching
trending repositories and developers. Relies on
[github-trending-api](https://github.com/huchenme/github-trending-api),
which is in JavaScript, so gtrending aims to fill the gap
for python.


```python
from gtrending import fetch_repos


repos = fetch_repos(language="python")  # get the result as a dict

for repo in repos:
    print(repo["fullname"])  # full name (user/repo) of each repo
```

The above example will fetch all the trending Python projects
on GitHub trending today and print their full names.


## Requirements
* Python 3.6 or higher


## Installation
```
pip3 install gtrending
```

## API

Documentation: [read the docs](https://gtrending.readthedocs.io/en/latest/)

### `fetch_repos()`

> Fetch trending repositories on GitHub

Parameters:
* `language (str, optional)`:  Filtering by language, eg: python
* `spoken_language_code (str, optional)`: The spoken language, eg: en for english
* `since (str, optional)`: The time range, choose from: [daily, weekly, monthly]. Defaults to "daily"

Returns:
> A list of dicts containing information for the trending repositories found


<br>

### `fetch_developers()`

> Fetch trending developers on GitHub

Parameters:
* `language (str, optional)`: The programming language, eg: python
* `since (str, optional)`: The time range, choose from [daily, weekly, monthly]. Defaults to "daily"

Returns:
> A list of dicts containing information for the trending repositories found

<br>

### `languages_list()`

> Fetch languages

Returns:
> A list of dictionaries containing languages

<br>

### `spoken_languages_list()`

> Fetch spoken languages

Returns:
> A list of spoken languages

<br>

### `check_language()`

> Check if the language exists

Parameters:
* `language (str)`:  The language, eg: python.

Returns:
> A boolean value. True for valid language, False otherwise.

<br>

### `check_spoken_language()`

> Check if the spoken language exists

Parameters:
* `spoken_language_code (str)`: The spoken language, eg: en for english.

Returns:
> A boolean value. True for valid spoken language, False otherwise.

<br>

### `check_since()`

> Check if the time range is correct

Parameters:
* `since (str)`:  The time range

Returns:
> A boolean value. True for valid parameter, False otherwise.
