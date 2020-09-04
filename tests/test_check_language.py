from gtrending import check_language


def assertions(response, expected):
    assert isinstance(response, bool)
    assert response == expected


def test_check_language():
    response = check_language("python")
    assertions(response, True)
    response = check_language("javascript")
    assertions(response, True)
    response = check_language("false_language")
    assertions(response, False)
