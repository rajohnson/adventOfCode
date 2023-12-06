import app


def test_calibrate():
    assert app.calibrate("1abc2") == 12
    assert app.calibrate("pqr3stu8vwx") == 38
    assert app.calibrate("a1b2c3d4e5f") == 15
    assert app.calibrate("treb7uchet") == 77


def test_calibrate_text():
    assert app.calibrate_text("two1nine") == 29
    assert app.calibrate_text("eightwothree") == 83
    assert app.calibrate_text("abcone2threexyz") == 13
    assert app.calibrate_text("xtwone3four") == 24
    assert app.calibrate_text("4nineeightseven2") == 42
    assert app.calibrate_text("zoneight234") == 14
    assert app.calibrate_text("7pqrstsixteen") == 76


def test_attempt():
    assert app.attempt("example.txt", 1) == 142
    assert app.attempt("example.txt", 2) == 281
