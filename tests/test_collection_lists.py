from gtrending import languages_list, spoken_languages_list


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
