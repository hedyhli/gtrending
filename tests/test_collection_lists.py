from gtrending import (
    languages_list,
    languages_dict,
    languages_params,
    languages_names,
    spoken_languages_list,
    spoken_languages_dict,
    spoken_languages_codes,
    spoken_languages_names,
)


def test_languages_list():
    response = languages_list()
    for i in response:
        assert isinstance(i, dict)
        assert len(i.keys()) == 2
        assert "param" in i.keys()
        assert "name" in i.keys()
        assert isinstance(i["param"], str)
        assert isinstance(i["name"], str)


def test_languages_dict():
    d = languages_dict()
    assert len(d) != 0
    for param, name in d.items():
        assert isinstance(param, str)
        assert isinstance(name, str)
        assert param
        assert name


def test_languages_params():
    l = languages_params()
    assert isinstance(l, list)
    for item in l:
        assert isinstance(item, str)
        assert item


def test_languages_names():
    l = languages_names()
    assert isinstance(l, list)
    for item in l:
        assert isinstance(item, str)
        assert item


def test_spoken_languages_list():
    response = spoken_languages_list()
    for i in response:
        assert isinstance(i, dict)
        assert len(i.keys()) == 2
        assert "code" in i.keys()
        assert "name" in i.keys()
        assert isinstance(i["code"], str)
        assert isinstance(i["name"], str)


def test_spoken_languages_dict():
    d = spoken_languages_dict()
    assert len(d) != 0
    for key in d.keys():
        assert isinstance(d[key], list)
        assert len(d[key]) != 0
        for i in d[key]:
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
