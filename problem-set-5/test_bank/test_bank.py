from bank import value

def test_hello():
    assert value("hello, putri") == 0
def test_hello_upper():
    assert value ("Hello, putri") == 0

def test_h():
    assert value("hermione, putri") == 20
def test_h_upper():
    assert value("Hermione, putri") == 20

def test_other():
    assert value("putri") == 100
def test_other_upper():
    assert value("Putri") == 100

def test_spaces():
    assert value("    putri") == 100

