from .fetch import (
    fetch_repos,
    fetch_developers,
)

from .paramutils import (
    languages_list,
    languages_params,
    languages_dict,
    languages_names,
    spoken_languages_list,
    spoken_languages_codes,
    spoken_languages_dict,
    spoken_languages_names,
    check_language,
    check_spoken_language_name,
    check_spoken_language_code,
    check_spoken_language,
    check_since,
    convert_spoken_language_name_to_code,
    convert_language_name_to_param,
)

__version__ = "0.4.0"
__url__ = "https://github.com/hedyhli/gtrending"
__author__ = "hedyhli"
__author_email__ = "hedy@tilde.cafe"
