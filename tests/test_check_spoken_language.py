from gtrending import check_spoken_language


def assertions(response, expected):
    assert isinstance(response, bool)
    assert response == expected


def test_check_language():
    response = check_spoken_language("en")
    assertions(response, True)
    response = check_spoken_language("es")
    assertions(response, True)
    response = check_spoken_language("notreal")
    assertions(response, False)
