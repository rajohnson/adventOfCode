import app


def test_calibrate():
    assert app.calibrate("1abc2") == 12
    assert app.calibrate("pqr3stu8vwx") == 38
    assert app.calibrate("a1b2c3d4e5f") == 15
    assert app.calibrate("treb7uchet") == 77


def test_attempt():
    assert app.attempt("example.txt") == 142
