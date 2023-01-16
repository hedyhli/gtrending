.. gtrending documentation master file, created by
   sphinx-quickstart on Tue Aug 11 09:36:45 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Documentation Home
==================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Fetch repositories and developers from `GitHub Trending
<https://github.com/trending>`_.

Here's a simple example, get the trending python projects and
display their full names::

    from gtrending import fetch_repos


    repos = fetch_repos(language="python")  # Returns a dictionary

    for repo in repos:
        print(repo["fullname"])  # "user/repo" for each repo


Installation
------------

Install gtrending on PyPI using your favorite package manage. For example::

    pip3 install gtrending

Contribute
----------

- Issue Tracker: https://github.com/hedyhli/gtrending/issues
- Source Code: https://github.com/hedyhli/gtrending

Support
-------

If you are having issues, please open an issue on the github issue tracker as linked above.


License
-------

The project is licensed under the MIT license.


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. toctree::
   :hidden:

   self
.. toctree::

   fetch/index
   paramutils/index
   API/index
