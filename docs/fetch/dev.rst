Trending Developers
===================


The ``fetch_developers()`` function can be used for fetching trending developers.

A **list of dictionaries** containing metadata about the trending developers as
well as the repository they are trending for is returned.


Parameters
----------

- ``language`` - the programming language to search for (eg: python)
- ``since`` - the date range for the search period. Either one of: **daily**, **weekly**, or **monthly**

.. note:: All parameters are case-insensitive

The default arguments are:

- ``language = ""`` (all languages included)
- ``since = "daily"``

The following are all valid examples:

.. testcode::

    fetch_developers()

    fetch_developers("python")

    fetch_developers(since="weekly")

    fetch_developers("rust", "monthly")


Example return values
---------------------
::

    [
      {
        "username": "stedolan",
        "name": "Stephen Dolan",
        "url": "https://github.com/stedolan",
        "sponsorUrl": null,
        "avatar": "https://avatars.githubusercontent.com/u/79765",
        "repo": {
          "name": "jq",
          "description": "Command-line JSON processor",
          "url": "https://github.com/stedolan/jq"
        }
      },
      {
        "username": "wcandillon",
        "name": "William Candillon",
        "url": "https://github.com/wcandillon",
        "sponsorUrl": null,
        "avatar": "https://avatars.githubusercontent.com/u/306134",
        "repo": {
          "name": "can-it-be-done-in-react-native",
          "description": "\u269b\ufe0f \ud83d\udcfa Projects from the \u201cCan it be done in React Native?\u201d YouTube series",
          "url": "https://github.com/wcandillon/can-it-be-done-in-react-native"
        }
      }
    ]


Argument validation
-------------------

The ``language`` parameter raises **ValueError** for invalid values.


Language
^^^^^^^^

Valid values must be one of the list of languages, returned from ``languages_params()``.

To check if a value is valid before passing to ``fetch_developers()``, use
``check_language(language)``

.. doctest::

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

