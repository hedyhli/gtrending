from gtrending import check_language


def assertions(response, expected):
    assert isinstance(response, bool)
    assert response == expected


def test_check_language():
    response = check_language("python", True)
    assertions(response)
    response = check_language("javascript", True)
    assertions(response)
    response = check_language("false_language", False)
    assertions(response)
