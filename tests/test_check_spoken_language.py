from gtrending import check_spoken_language


def assertions(response, expected):
    assert isinstance(response, bool)
    assert response == expected


def test_check_language():
    response = check_spoken_language("en", True)
    assertions(response)
    response = check_spoken_language("es", True)
    assertions(response)
    response = check_spoken_language("notreal", False)
    assertions(response)
