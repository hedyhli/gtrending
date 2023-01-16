Language parameter
==================

The function ``languages_list()`` returns a list of supported programming
languages that can be used for search in fetching trending :doc:`repositories
<../fetch/repo>` and :doc:`developers <../fetch/dev>`::

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


**NOTE**:
