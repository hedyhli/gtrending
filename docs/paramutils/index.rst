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
are raised if the argument is truthy, yet ``False`` returned when passed to
corresponding ``check_*()`` functions.

----

Detailed usage
--------------

.. toctree::

    language
    spoken-language
