import pytest

from gtrending import convert_spoken_language_name_to_code


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
