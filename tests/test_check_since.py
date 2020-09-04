from gtrending import check_since


def assertions(response, expected):
    assert isinstance(response, bool)
    assert response == expected


def test_check_language():
    response = check_since("daily")
    assertions(response, True)
    response = check_since("weekly")
    assertions(response, True)
    response = check_since("annually")
    assertions(response, False)
