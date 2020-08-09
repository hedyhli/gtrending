# `gtrending`

![checks](https://github.com/hedythedev/starcli/workflows/checks/badge.svg)
[![codecov](https://codecov.io/gh/hedythedev/gtrending/branch/master/graph/badge.svg?token=J19AQKEO4W)](https://codecov.io/gh/hedythedev/gtrending)
[![pypi version](https://img.shields.io/pypi/v/gtrending)](https://pypi.org/project/gtrending/)
[![Python Requirements](https://img.shields.io/pypi/pyversions/gtrending)](https://pypi.org/project/gtrending/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Lightweight and easy-to-use python library for fetching
trending repositories and developers. Relies on
[github-trending-api](https://github.com/huchenme/github-trending-api)
which is in JavaScript, so gtrending aims to fill the gap
for python.

### Simple Demo

```python
from gtrending import fetch_repos

repos = fetch_repos(language="python")
for repo in repos:
    print(repo["fullname"])
```

The above example will print all the trending Python projects
on GitHub, trending today, and print their full names.

### Requirements
* Python 3.6 or higher


### Installation
```
pip3 install gtrending
```

### api
Work in progress...
