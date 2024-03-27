import plates

def test_start():
    assert plates.is_valid("P9UTRI") == False
    assert plates.is_valid("9PUTRI") == False
    assert plates.is_valid("99PUTR") == False
    assert plates.is_valid("PPPUTR") == True
    assert plates.is_valid(".PUTRI") == False
    assert plates.is_valid(".,PUTR") == False
    assert plates.is_valid("613BTS") == False
    assert plates.is_valid("50") == False

def test_length():
    assert plates.is_valid("PPPUTRI") == False
    assert plates.is_valid("PUT197") == True
    assert plates.is_valid("P") == False


def test_numb():
    assert plates.is_valid("AAA222") == True
    assert plates.is_valid("AAA22A") == False
    assert plates.is_valid("AAA022") == False


def test_char():
    assert plates.is_valid("PUT.RI") == False
    assert plates.is_valid(" PUTRI") == False