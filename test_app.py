from App import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_and_positive():
    assert add(-1, 1) == 0

def test_add_zeros():
    assert add(0, 0) == 0
