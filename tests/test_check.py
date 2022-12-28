import pytest

from gtrending import (
    check_language,
    check_spoken_language,
    check_spoken_language_name,
    check_spoken_language_code,
    check_since,
)


def test_check_language():
    assert check_language("python")
    assert check_language("JavaScript")
    assert check_language("1c-enterprise")
    assert check_language("1c-Enterprise")
    assert not check_language("1c enterprise")
    assert check_language("c#")
    assert check_language("c++")
    assert check_language("c")
    assert check_language("world-of-warcraft-addon-data")
    assert check_language("HTML+Django")
    assert not check_language("HTML%2BDjango")
    assert not check_language("c%23")
    assert not check_language("")
    assert not check_language("false_language")


@pytest.mark.xfail()
def test_check_language_special():
    # FIXME: "'" is quoted, but the urlParam value in languages_list() is not
    assert check_language("cap'n-proto")


def test_check_spoken_language():
    assert check_spoken_language("en")
    assert check_spoken_language("ES")
    assert check_spoken_language("English")
    assert check_spoken_language("spanish")
    assert not check_spoken_language("")
    assert not check_spoken_language("notreal")


def test_check_spoken_language_code():
    assert check_spoken_language_code("EN")
    assert check_spoken_language_code("es")
    assert check_spoken_language_code("zh")
    assert check_spoken_language_code("el")
    assert not check_spoken_language_code("")
    assert not check_spoken_language_code("xx")
    assert not check_spoken_language_code("english")
    assert not check_spoken_language_code("Spanish")


def test_check_spoken_language_name():
    assert not check_spoken_language_name("EN")
    assert not check_spoken_language_name("es")
    assert not check_spoken_language_name("zh")
    assert not check_spoken_language_name("el")
    assert not check_spoken_language_name("xx")
    assert not check_spoken_language_name("")
    assert check_spoken_language_name("english")
    assert check_spoken_language_name("Spanish")
    assert check_spoken_language_name("GREEK")
    assert not check_spoken_language_name("notreal")


def test_check_since():
    assert check_since("daily")
    assert check_since("weekly")
    assert not check_since("annually")
    assert not check_since("")
