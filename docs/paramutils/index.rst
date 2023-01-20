Utilities
=========

The ``gtrending.paramutils`` module provides utility functions for search
parameters, including:

- ``language``,
- ``spoken_language_code``, and
- ``since``.


Terminology
-----------

For ``language`` and ``spoken_language_code``, only values in the required form
is accepted. For example, ``emacs-lisp`` instead of ``Emacs Lisp``, or ``es``
instead of ``Spanish``.

These values can be validated using functions with the corresponding prefix
``language_*()`` or ``spoken_language_*()`` in this module.

For **language**: The parameter value that should be used is named **"param"**.

For **spoken language**: The parameter value that should be used is named **"code"**.

The full name of both of these parameters, are named **"name"**.

.. list-table:: TLDR
   :header-rows: 1
   :widths: 30 50 20

   * - Name
     - Meaning
     - Example
   * - Language name
     - Full name of language
     - "Common Lisp"
   * - Language param
     - Value used in :doc:`fetch <../fetch/index>` functions
     - *"common-lisp"*
   * - Spoken language name
     - Full name of spoken language
     - "Italian"
   * - Spoken language code
     - 2-character code for spoken language;

       Value used in :doc:`fetch <../fetch/index>` functions
     - *"it"*

Values in *italics* indicate the value format that must be used in the fetch module.

.. note::
   The ``since`` parameter has only one form, it can only be one of "daily",
   "weekly", or "monthly".


Conversion
----------

Hence, conversion between the two formats may be done using ``convert_*()`` functions:

- ``convert_language_name_to_param()`` Converts a given name of a programming
  language, eg: "Emacs Lisp", into the correct parameter form to be used when
  calling functions in :doc:`gtrending.fetch module <../fetch/index>`, eg:
  "emacs-lisp".
- ``convert_spoken_language_name_to_code()`` Converts a given name of a spoken
  language, eg: "Spanish", into the correct parameter form (the language code),
  eg: "es"


Validation
----------

Functions that can be used to validate arguments before passing to fetch-functions
have the prefix ``check_*()``.

.. note::
    If an empty string is passed as an argument to these functions, ``False``
    is returned, **even though all parameters are optional in the fetch
    module**.

- ``check_language()`` checks that the argument is a valid language parameter
- ``check_spoken_language()`` checks that the argument is a valid spoken
  language code
- ``check_since()`` checks that the argument is one of the valid options for
  date range: daily, weekly, and monthly.


These functions are called from within fetch-functions, where **ValueError**\ s
are raised if: the argument is truthy, AND ``False`` returned when passed to
corresponding ``check_*()`` functions.

For example, the following WILL raise ValueError::

    fetch_repos("does-not-exist")
    fetch_developers("common lisp")
    fetch_developers(since="yearly")
    fetch_repos(spoken_language_code="English")

And the following WILL NOT raise ValueError:

.. testcode::

    fetch_repos("")
    fetch_developers(since=None)
    fetch_developers(language="css")


Lists and dictionaries
----------------------

Languages List - A list of dictionaries with param and name.::

    >>> languages_list()
    [
      {
        "param": "1c-enterprise",
        "name": "1C Enterprise"
      },
      {
        "param": "abap",
        "name": "ABAP"
      },

      ...

      {
        "param": "yara",
        "name": "YARA"
      },
      {
        "param": "zephir",
        "name": "Zephir"
      },
      {
        "param": "zimpl",
        "name": "Zimpl"
      },
    ]

Languages Dictionary - A dictionary of each param to its full name.::

    >>> languages_dict()
    {
        '1c-enterprise': '1C Enterprise',
        'abap': 'ABAP',
        'abnf': 'ABNF',
        ...
        'yara': 'YARA',
        'zephir': 'Zephir',
        'zimpl': 'Zimpl'
    }

Spoken Languages List - A list of dictionaries of code and the list of names.::

    >>> spoken_languages_list()
    [
        {'code': 'ab', 'name': ['Abkhazian']},
        {'code': 'aa', 'name': ['Afar']},
        {'code': 'af', 'name': ['Afrikaans']},
        {'code': 'ak', 'name': ['Akan']},
        ...
        {'code': 'yo', 'name': ['Yoruba']},
        {'code': 'za', 'name': ['Zhuang', 'Chuang']},
        {'code': 'zu', 'name': ['Zulu']}
    ]

Spoken Languages Dictionary - A dictionary of the languages codes to its list of names.::

    >>> spoken_languages_dict()
    {
        'aa': ['Afar'],
        'ab': ['Abkhazian'],
        'ae': ['Avestan'],
        'af': ['Afrikaans'],
        ...
        'yi': ['Yiddish'],
        'yo': ['Yoruba'],
        'za': ['Zhuang', 'Chuang'],
        'zh': ['Chinese'],
        'zu': ['Zulu'],
    }
