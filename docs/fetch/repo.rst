Trending Repositories
=====================

The ``fetch_repos()`` function can be used for fetching trending repositories on GitHub.


A **list of dictionaries** containing metadata about the trending repositories is returned.

Parameters
----------

- ``language`` - the programming language to search for (eg: python)
- ``spoken_language_code`` - the code of the spoken language to search for (eg: en)
- ``since`` - the date range for the search period. Either one of: **daily**, **weekly**, and **monthly**

.. note:: All parameters are case-insensitive

The default arguments are:

- ``language = ""`` (all languages included)
- ``spoken_language_code = ""`` (all spoken languages included)
- ``since = "daily"`` (trending today)

The following are all valid examples::

    fetch_repos()

    fetch_repos("javascript")
    fetch_repos(spoken_language_code="zh")
    fetch_repos(since="monthly")

    fetch_repos("javascript", "zh", "monthly")


Example return values
---------------------
::

    [
      {
        "author": "ShoufaChen",
        "name": "DiffusionDet",
        "avatar": "https://github.com/ShoufaChen.png",
        "description": "PyTorch implementation of DiffusionDet (https://arxiv.org/abs/2211.09788)",
        "url": "https://github.com/ShoufaChen/DiffusionDet",
        "language": "Python",
        "languageColor": "#3572A5",
        "stars": 610,
        "forks": 19,
        "currentPeriodStars": 121,
        "builtBy": [
          {
            "username": "ShoufaChen",
            "href": "https://github.com/ShoufaChen",
            "avatar": "https://avatars.githubusercontent.com/u/28682908"
          }
        ],
        "fullname": "ShoufaChen/DiffusionDet"
      },
      {
        "author": "FlagAI-Open",
        "name": "FlagAI",
        "avatar": "https://github.com/FlagAI-Open.png",
        "description": "FlagAI (Fast LArge-scale General AI models) is a fast, easy-to-use and extensible t
      oolkit for large-scale model.",
        "url": "https://github.com/FlagAI-Open/FlagAI",
        "language": "Python",
        "languageColor": "#3572A5",
        "stars": 323,
        "forks": 42,
        "currentPeriodStars": 38,
        "builtBy": [
          {
            "username": "marscrazy",
            "href": "https://github.com/marscrazy",
            "avatar": "https://avatars.githubusercontent.com/u/4392184"
          },
          {
            "username": "Anhforth",
            "href": "https://github.com/Anhforth",
            "avatar": "https://avatars.githubusercontent.com/u/94831503"
          },
          {
            "username": "920232796",
            "href": "https://github.com/920232796",
            "avatar": "https://avatars.githubusercontent.com/u/32668889"
          },
          {
            "username": "ZhaodongYan1",
            "href": "https://github.com/ZhaodongYan1",
            "avatar": "https://avatars.githubusercontent.com/u/26128888"
          },
          {
            "username": "BAAI-OpenPlatform",
            "href": "https://github.com/BAAI-OpenPlatform",
            "avatar": "https://avatars.githubusercontent.com/u/107522723"
          }
        ],
        "fullname": "FlagAI-Open/FlagAI"
      },
    ]


The key ``currentPeriodStars`` is the increase of stars for the current
trending period - as specified by the ``since`` argument.


Argument validation
-------------------

Parameters ``language`` and ``spoken_language_code`` only accept valid values.
**ValueError** is thrown for invalid values.

Both parameters are case-insensitive.

Language
^^^^^^^^

Valid values must be one of the list of languages, returned from ``languages_params()``.

To check if a value is valid before passing to ``fetch_repos()``, use ``check_language(language)``::

    >>> check_language("python")
    True
    >>> check_language("Ruby")
    True
    >>> check_language("TeaScript")  # Does not exist
    False
    >>> check_language("")
    False

See the :doc:`ParamUtils module <../paramutils/index>` for usage details on parameter
validation functions.


Spoken language code
^^^^^^^^^^^^^^^^^^^^

Valid values must be one of the list of spoken language codes, returned from
``spoken_languages_codes()``.

.. note::
   This is the spoken language code, as in "en"/"es"/"ko", and not the spoken
   language name itself (such as "english").


To check if a value is valid before passing to ``fetch_repos()``, use
``check_spoken_language_code(code)``

.. doctest::

    >>> check_spoken_language_code("el")
    True
    >>> check_spoken_language_code("ZH")
    True
    >>> check_spoken_language_code("ZZ")  # Does not exist
    False
    >>> check_spoken_language_code("")
    False


See the :doc:`ParamUtils module <../paramutils/index>` for functions that validate the
spoken language name, and convert between the name and the code.
