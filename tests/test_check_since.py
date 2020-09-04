from gtrending import check_since


def assertions(response, expected):
    assert isinstance(response, bool)
    assert response == expected


def test_check_language():
    response = check_since("daily", True)
    assertions(response)
    response = check_since("weekly", True)
    assertions(response)
    response = check_since("annually", False)
    assertions(response)
