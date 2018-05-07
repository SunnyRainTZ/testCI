def add(a, b):
    return a - b


def test_add_one():
    assert add(1, 2) == 3


def test_add_two():
    assert add(3, 5) == 8
