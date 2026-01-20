from model import double

def test_double_integer():
    result = double(13)
    assert 26 == result


def test_double_integer2():
    result = double(17)
    assert 34 == result
