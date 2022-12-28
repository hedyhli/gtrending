import pytest

from gtrending import (
    convert_spoken_language_name_to_code,
    convert_language_name_to_param,
)


@pytest.mark.parametrize(
    "name,code",
    [
        ("Spanish", "es"),
        ("Italian", "it"),
        ("Chinese", "zh"),
        ("notreal", ""),
        ("en", ""),
        ("", ""),
    ],
)
def test_convert_spoken_language_name_to_code(name, code):
    assert code == convert_spoken_language_name_to_code(name)


@pytest.mark.parametrize(
    "name,param",
    [
        ("Python", "python"),
        ("common lisp", "common-lisp"),
        ("C#", "c#"),
        ("c++", "c++"),
        ("Visual basic", "visual-basic"),
        # ("Visual Basic 6.0", "visual-basic-6.0"),
        # ("visual basic .net", "visual-basic-.net"),
        ("graphviz (dot)", "graphviz-(dot)"),
        ("html+django", "html+django"),
        ("does not exist", ""),
    ]
)
def test_convert_language_name_to_param(name, param):
    assert param == convert_language_name_to_param(name)
