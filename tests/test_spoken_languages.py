from gtrending import spoken_languages_list


def assertions(response):
    assert isinstance(response, list)
    for i in response:
        assert isinstance(i, dict)
        for key in i.keys():
            assert isinstance(key, str)
            assert isinstance(i[key], str)


def test_spoken_languages_list():
    response = spoken_languages_list()
    assertions(response)