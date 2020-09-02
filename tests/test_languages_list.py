from gtrending import languages_list


def assertions(response):
    assert isinstance(response, list)
    for i in response:
        assert isinstance(i, dict)
        for key in i.keys():
            assert isinstance(key, str)
            assert isinstance(i[key], str)

def test_language_list():
    response = languages_list()
    assertions(response)