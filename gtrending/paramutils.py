"""Parameter utility functions"""

from urllib.parse import unquote as urlunquote
from typing import List

import requests


"""Tuple of valid arguments for the `since` parameter"""
SINCE_PARAM = ("daily", "weekly", "monthly")


def languages_list() -> List[dict]:
    """Fetch programming languages.

    Example:
        ::

            [
                {'name': '1C Enterprise', 'param': '1c-enterprise'},
                {'name': 'ABAP', 'param': 'abap'},
                {'name': 'ABNF', 'param': 'abnf'},
                ...
                {'name': 'HTML+ERB', 'param': 'html+erb'},
                {'name': 'HTML+PHP', 'param': 'html+php'},
                {'name': 'HTTP', 'param': 'http'},
                {'name': 'Hy', 'param': 'hy'},
                {'name': 'HyPhy', 'param': 'hyphy'},
                {'name': 'IDL', 'param': 'idl'},
                {'name': 'Idris', 'param': 'idris'},
                {'name': 'IGOR Pro', 'param': 'igor-pro'},
                {'name': 'Inform 7', 'param': 'inform-7'},
                {'name': 'INI', 'param': 'ini'},
                {'name': 'Inno Setup', 'param': 'inno-setup'},
                {'name': 'Io', 'param': 'io'},
                {'name': 'Ioke', 'param': 'ioke'},
                {'name': 'IRC log', 'param': 'irc-log'},
                ...
            ]

    Returns:
        list(dict): A list of dictionaries containing languages, mapping the param value to its name
    """
    url: str = "https://gtrend.yapie.me/languages"
    response = requests.get(url).json()

    # Rename key urlParam to param
    for i in response:
        # https://stackoverflow.com/questions/54637847/how-to-change-dictionary-keys-in-a-list-of-dictionaries
        i["param"] = urlunquote(i.pop("urlParam"))
        # urlParam values returned by API shows values that should be used as
        # url query values, these are converted to %-decoded values for use as
        # a python library.
        #
        # (For check_language()):

    return response


def spoken_languages_list() -> List[dict]:
    """Fetch spoken languages.

    Example:
        ::

            [
                ...
                {'code': 'bh', 'name': ['Bihari languages']},
                ...
                {'code': 'ca', 'name': ['Catalan', 'Valencian']},
                {'code': 'ch', 'name': ['Chamorro']},
                {'code': 'ce', 'name': ['Chechen']},
                {'code': 'ny', 'name': ['Chichewa', 'Chewa', 'Nyanja']},
                {'code': 'zh', 'name': ['Chinese']},
                ...
                {'code': 'cs', 'name': ['Czech']},
                {'code': 'da', 'name': ['Danish']},
                {'code': 'dv', 'name': ['Divehi', 'Dhivehi', 'Maldivian']},
                {'code': 'nl', 'name': ['Dutch', 'Flemish']},
                {'code': 'dz', 'name': ['Dzongkha']},
                {'code': 'en', 'name': ['English']},
                {'code': 'eo', 'name': ['Esperanto']},
                {'code': 'et', 'name': ['Estonian']},
                ...
                {'code': 'de', 'name': ['German']},
                {'code': 'el', 'name': ['Greek', 'Modern']},
                ...
            ]

    Returns:
        list(dict): A list dictionaries of spoken languages, mapping the code to the name
    """
    url: str = "https://gtrend.yapie.me/spoken_languages"
    response = requests.get(url).json()

    # Rename key urlParam to code
    for i in response:
        # https://stackoverflow.com/questions/54637847/how-to-change-dictionary-keys-in-a-list-of-dictionaries
        i["code"] = i.pop("urlParam")
        i["name"] = i["name"].split(", ")

    return response


def check_language(language: str) -> bool:
    """Check if the language parameter is valid.

    Value that is already url-encoded would not be accepted.

    Returns false for falsey values.

    Examples:
        >>> check_language('python')
        True
        >>> check_language('py')
        False
        >>> check_language('GO')
        True
        >>> check_language('c%2B%2B')
        False
        >>> check_language('c++')
        True
        >>> check_language('')
        False
        >>> check_language('vim-script')
        True

    Parameters:
        language (str):  The language, eg: python (case-insensitive)

    Returns:
        bool: True for valid language, False otherwise
    """
    if not language:
        return False

    languages = languages_list()
    language = language.lower()

    for name in languages:
        if language == name["param"]:
            return True

    return False


def convert_language_name_to_param(language: str) -> str:
    """Convert language name to value used as API parameter

    Examples:
        >>> convert_language_name_to_param('Python')
        'python'
        >>> convert_language_name_to_param('')
        ''
        >>> convert_language_name_to_param('perl 6')
        'perl-6'
        >>> convert_language_name_to_param('c++')
        'c++'
        >>> convert_language_name_to_param('C#')
        'c#'

    Parameters:
        language (str): The language name, eg: "Vim script"

    Returns:
        str: The language in parameter format, eg: vim-script
    """
    langs = languages_list()
    for lang in langs:
        if language.lower() == lang["name"].lower():
            return lang["param"]

    # TODO: is ValueError better?
    return ""


def languages_dict() -> dict:
    """Dictionary of the language param for its name.

    Example:
        ::

            {
                ...
                'restructuredtext': 'reStructuredText',
                'rexx': 'REXX',
                'rhtml': 'RHTML',
                'ring': 'Ring',
                'rmarkdown': 'RMarkdown',
                'robotframework': 'RobotFramework',
                'roff': 'Roff',
                'rouge': 'Rouge',
                'rpc': 'RPC',
                'rpm-spec': 'RPM Spec',
                'ruby': 'Ruby',
                'runoff': 'RUNOFF',
                'rust': 'Rust',
                'sage': 'Sage',
                'saltstack': 'SaltStack',
                'sas': 'SAS',
                'sass': 'Sass',
                'scala': 'Scala',
                'scaml': 'Scaml',
                'scheme': 'Scheme',
                'scilab': 'Scilab',
                'scss': 'SCSS',
                'sed': 'sed',
                'self': 'Self',
                'shaderlab': 'ShaderLab',
                'shell': 'Shell',
                ...
            }

    Returns:
        dict: ``param: name`` for each language
    """
    lang_dict = {}
    for entry in languages_list():
        lang_dict[entry.get("param")] = entry.get("name")
    return lang_dict


def languages_params() -> List[str]:
    """List of valid language params.

    Example:
        ::

            [..., "html", "makefile", "lua", "m4", "mathematica", "emacs-lisp", ...]

    Returns:
        list(str): List of languages' params as strings
    """
    return list(languages_dict().keys())


def languages_names() -> list:
    """List of valid language names.

    Example:
        ::

            [..., "HTML", "Makefile", "Lua", "M4", "Mathematica", "Emacs Lisp", ...]

    Returns:
        list(str): List of capitalized names as strings
    """
    names = []
    for val in languages_dict().values():
        names.append(val)
    return names


def spoken_languages_dict() -> dict:
    """Dictionary of the spoken language code for its name

    Example:
        ::

            {
                ...
                'nl': ['Dutch', 'Flemish'],
                'nn': ['Norwegian Nynorsk'],
                'no': ['Norwegian'],
                'nr': ['South Ndebele'],
                'nv': ['Navajo', 'Navaho'],
                'ny': ['Chichewa', 'Chewa', 'Nyanja'],
                'oc': ['Occitan'],
                'oj': ['Ojibwa'],
                'om': ['Oromo'],
                'or': ['Oriya'],
                'os': ['Ossetian', 'Ossetic'],
                'pa': ['Punjabi', 'Panjabi'],
                'pi': ['Pali'],
                'pl': ['Polish'],
                'ps': ['Pashto', 'Pushto'],
                'pt': ['Portuguese'],
                'qu': ['Quechua'],
                'rm': ['Romansh'],
                'rn': ['Rundi'],
                'ro': ['Romanian', 'Moldavian', 'Moldovan'],
                'ru': ['Russian'],
                'rw': ['Kinyarwanda'],
                'sa': ['Sanskrit'],
                'sc': ['Sardinian'],
                'sd': ['Sindhi'],
                'se': ['Northern Sami'],
                'sg': ['Sango'],
                'si': ['Sinhala', 'Sinhalese'],
                'sk': ['Slovak'],
                ...
            }

    Returns:
        dict: ``code: [names, ...]`` for each spoken language
    """
    sl_d = {}
    for entry in spoken_languages_list():
        sl_d[entry.get("code")] = entry.get("name")
    return sl_d


def spoken_languages_codes() -> list:
    """List of valid spoken language codes

    Example:
        ::
            ["en", "es", "it", "fr", ...]

    Returns:
        list(str): 2-character codes as strings
    """
    sl_d = spoken_languages_dict()
    return list(sl_d.keys())


def spoken_languages_names() -> List[str]:
    """List of valid spoken language names

    Example:
        ::
            ["English", "Spanish", "Italian", "French", ...]

    Returns:
        list(str): Capitalized spoken language names as strings
    """
    sl_d = spoken_languages_dict()
    names = []
    for name in sl_d.values():
        names.extend(name)
    return names


def convert_spoken_language_name_to_code(sl_name: str) -> str:
    """Convert spoken language name to its code.

    Returns an empty string for an invalid name.

    Examples:
        >>> convert_spoken_language_name_to_code('Greek')
        'el'
        >>> convert_spoken_language_name_to_code('French')
        'fr'

    Parameters:
        sl_name (str): The spoken language name

    Returns:
        str: The corresponding spoken_language code
    """
    sl_d = spoken_languages_dict()
    for code, names in sl_d.items():
        if sl_name in names:
            return code

    # TODO: is ValueError better?
    return ""


def check_spoken_language_name(spoke_language: str) -> bool:
    """Check if the spoken language name exists, case-insensitive.

    Returns false for falsey values.

    Examples:
        >>> check_spoken_language_name('english')
        True
        >>> check_spoken_language_name('en')
        False
        >>> check_spoken_language_name('Greek')
        True
        >>> check_spoken_language_name('')
        False

    Parameters:
        sl (str): The spoken language, eg: English, Spanish

    Returns:
        bool: True for valid spoken language name, False otherwise
    """
    if not spoke_language:
        return False
    spoken_language = spoke_language.lower()
    return spoken_language in [i.lower() for i in spoken_languages_names()]


def check_spoken_language_code(code: str) -> bool:
    """Check if the spoken language code exists, case-insensitive.

    Returns false for falsey values.

    Examples:
        >>> check_spoken_language_code('english')
        False
        >>> check_spoken_language_code('en')
        True
        >>> check_spoken_language_code('EL')
        True
        >>> check_spoken_language_code('py')
        False

    Parameters:
        sl (str): The spoken language code, eg: en, es

    Returns:
        bool: True for valid spoken language code, False otherwise.
    """
    if not code:
        return False
    code = code.lower()
    return code in spoken_languages_codes()


def check_spoken_language(spoken_language: str) -> bool:
    """Check if the spoken language code or name exists.

    Returns false for falsey values

    Examples:
        >>> check_spoken_language('english')
        True
        >>> check_spoken_language('en')
        True
        >>> check_spoken_language('EL')
        True
        >>> check_spoken_language('python')
        False

    Parameters:
        sl (str): The spoken language, eg: English, or en for English

    Returns:
        bool: True for valid spoken language, False otherwise
    """
    if not spoken_language:
        return False
    return check_spoken_language_code(spoken_language) or check_spoken_language_name(
        spoken_language
    )


def check_since(since: str) -> bool:
    """Check if the time range value is correct.

    Examples:
        >>> check_since('daily')
        True
        >>> check_since('DAILY')
        True
        >>> check_since('yearly')
        False

    Parameters:
        since (str): The time range

    Returns:
        bool: True for valid parameter, False otherwise
    """
    return since.lower() in SINCE_PARAM
