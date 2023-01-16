Fetch Module
============

The ``gtrending.fetch`` module includes functions for fetching trending
repositories and developers from GitHub Trending.

.. toctree::
   :maxdepth: 1

   repo
   dev

Optional parameters to specify the programming language, spoken language, and
the date range can be used.


Parameters
----------

All parameters are case-insensitive.

- **Programming language**: ``language`` (str), eg: "python", "vimscript".

  This specifies the primary language that repositories are written in, when
  searching trending repositories, and the primary language a developer's
  trending repository is written in, when searching for trending developers

- **Spoken language**: ``spoken_language_code`` (str), eg: "en", "es".

  This specifies the primary spoken language of the trending repository, or of
  the trending developer's repository.

- **Date range**: ``since`` (str). Must be one of daily, weekly, or monthly.

  The date range of which the repository or developer is trending for. This
  parameter affects the ``currentPeriodStars`` value of the resulting list of
  dictionaries returned. See the documentation page of :doc:`fetch_repos()
  function <repo>` for details.


Helper functions for the validation of these parameters are available in the
:doc:`ParamUtils module <../paramutils/index>`


Return values
-------------

Where a list of dictionaries are returned, here are the keys in each dictionary for repositories::

    author              str
    name                str
    avatar              str (url)
    description         str
    url                 str
    language            str
    languageColor       str (hex)
    stars               int
    forks               int
    currentPeriodStars  int (stars increase for date range)
    builtBy             list (dicts)
        username            str
        href                str
        avatar              str (url)
    fullname            str ("user/repo")

And here are the keys for developers::

    username         str
    name             str
    url              str
    sponsorUrl       str
    avatar           str (url)
    repo             dict
        name             str
        description      str
        url              str
