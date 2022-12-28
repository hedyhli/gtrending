from urllib.parse import quote as urlquote, unquote as urlunquote

import requests


"""Tuple of valid arguments for the `since` parameter"""
SINCE_PARAM = ("daily", "weekly", "monthly")


def languages_list() -> list:
    """Fetch programming languages.

    Returns:
        A list of dictionaries containing languages.
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


def spoken_languages_list() -> list:
    """Fetch spoken languages.

    Returns:
        A list of spoken languages.
    """
    url: str = "https://gtrend.yapie.me/spoken_languages"
    response = requests.get(url).json()

    # Rename key urlParam to code
    for i in response:
        # https://stackoverflow.com/questions/54637847/how-to-change-dictionary-keys-in-a-list-of-dictionaries
        i["code"] = i.pop("urlParam")

    return response


def check_language(language: str) -> bool:
    """Check if the language parameter is valid

    Value that is already url-encoded would not be accepted.

    Returns false for falsey values

    Parameters:
        language (str):  The language, eg: python.

    Returns:
        A boolean value. True for valid language, False otherwise.
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

    Parameters:
        language (str): The language name, eg: "Vim script"

    Returns:
        The language in parameter format, eg: vim-script
    """
    langs = languages_list()
    for lang in langs:
        if language.lower() == lang["name"].lower():
            return lang["param"]

    # TODO: is ValueError better?
    return ""


def languages_dict() -> dict:
    """Dictionary of the language param for its name"""
    sl = {}
    for entry in languages_list():
        sl[entry.get("param")] = entry.get("name")
    return sl


def languages_params() -> list:
    """List of valid language params"""
    ld = languages_dict()
    return list(ld.keys())


def languages_names() -> list:
    """List of valid language names"""
    ld = languages_dict()
    names = []
    for param in ld.keys():
        names.extend(ld[param])
    return names


def spoken_languages_dict() -> dict:
    """Dictionary of the spoken language code for its name

    For example,

        {
            "python": "Python",
            "vim-script": "Vim script",
            "visual-basic": "Visual Basic",
            ...
        }
    """
    sl = {}
    for entry in spoken_languages_list():
        sl[entry.get("code")] = entry.get("name").split(", ")
    return sl


def spoken_languages_codes() -> list:
    """List of valid spoken language codes

    For example,

        ["en", "es", "it", "fr"]
    """
    sl = spoken_languages_dict()
    return list(sl.keys())


def spoken_languages_names() -> list:
    """List of valid spoken language names

    For example,

        ["English", "Spanish", "Italian", "French"]
    """
    sl = spoken_languages_dict()
    names = []
    for code in sl.keys():
        names.extend(sl[code])
    return names


def convert_spoken_language_name_to_code(sl_name: str) -> str:
    """Convert spoken language name to its code.

    Returns an empty string for invalid name.

    For example,

    >>> convert_spoken_language_name_to_code("Greek")
    "el"
    >>> convert_spoken_language_name_to_code("French")
    "fr"

    Parameters:
        sl_name (str): The spoken language name

    Returns:
        A string - the corresponding spoken_language code.
    """
    sl = spoken_languages_dict()
    for code in sl.keys():
        if sl_name in sl[code]:
            return code

    # TODO: is ValueError better?
    return ""


def check_spoken_language_name(sl: str) -> bool:
    """Check if the spoken language name exists, case-insensitive.

    Returns false for falsey values

    Parameters:
        sl (str): The spoken language, eg: English, Spanish

    Returns:
        A boolean value. True for valid spoken language name, False otherwise.
    """
    if not sl:
        return False
    sl = sl.lower()
    return sl in [i.lower() for i in spoken_languages_names()]


def check_spoken_language_code(sl: str) -> bool:
    """Check if the spoken language code exists, case-insensitive.

    Returns false for falsey values

    Parameters:
        sl (str): The spoken language code, eg: en, es

    Returns:
        A boolean value. True for valid spoken language code, False otherwise.
    """
    if not sl:
        return False
    sl = sl.lower()
    return sl in spoken_languages_codes()


def check_spoken_language(sl: str) -> bool:
    """Check if the spoken language code or name exists.

    Returns false for falsey values

    Parameters:
        sl (str): The spoken language, eg: English, or en, for English.

    Returns:
        A boolean value. True for valid spoken language, False otherwise.
    """
    if not sl:
        return False
    return check_spoken_language_code(sl) or check_spoken_language_name(sl)


def check_since(since: str) -> bool:
    """Check if the time range value is correct.

    Parameters:
        since (str): The time range.

    Returns:
        A boolean value. True for valid parameter, False otherwise.
    """
    return since.lower() in SINCE_PARAM
