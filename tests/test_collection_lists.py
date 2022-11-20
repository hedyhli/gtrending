from gtrending import (
    languages_list,
    spoken_languages_list,
    spoken_languages_dict,
    spoken_languages_codes,
    spoken_languages_names,
)


def test_language_list():
    response = languages_list()
    for i in response:
        assert isinstance(i, dict)
        for key in i.keys():
            assert isinstance(key, str)
            assert isinstance(i[key], str)


def test_spoken_languages_list():
    response = spoken_languages_list()
    for i in response:
        assert isinstance(i, dict)
        for key in i.keys():
            assert isinstance(key, str)
            assert isinstance(i[key], str)


def test_spoken_languages_dict():
    d = spoken_languages_dict()
    assert len(d) != 0
    for key in d.keys():
        assert isinstance(d.get(key), list)
        assert len(d.get(key)) != 0
        for i in d.get(key):
            assert isinstance(i, str)
            assert len(i) != 0


def test_spoken_languages_codes():
    l = spoken_languages_codes()
    assert isinstance(l, list)
    assert len(l) != 0
    for i in l:
        assert isinstance(i, str)
        assert len(i) == 2
        assert i.lower() == i


def test_spoken_languages_names():
    l = spoken_languages_names()
    assert isinstance(l, list)
    assert len(l) != 0
    for i in l:
        assert isinstance(i, str)
        assert len(i) > 2
        assert i.lower() != i
