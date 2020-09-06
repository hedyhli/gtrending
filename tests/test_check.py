from gtrending import check_language, check_spoken_language, check_since


def test_check_language():
    assert check_language("python")
    assert check_language("javascript")
    assert not check_language("false_language")


def test_check_spoken_language():
    assert check_spoken_language("en")
    assert check_spoken_language("es")
    assert not check_spoken_language("notreal")


def test_check_since():
    assert check_since("daily")
    assert check_since("weekly")
    assert not check_since("annually")
