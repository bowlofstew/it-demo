def add(this, that):
    result = this + that
    return result


def test_add():
    assert add(10, 15) == 25
