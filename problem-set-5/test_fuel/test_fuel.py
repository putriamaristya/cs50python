import fuel
import pytest

def test_fraction():
    assert fuel.convert("1/2") == 50

def test_value_error():
    with pytest.raises(ValueError):
        fuel.convert("cat/dog")
    with pytest.raises(ValueError):
        fuel.convert("4/3")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("4/0")

def test_1():
    assert fuel.gauge(1) == "E"

def test_100():
    assert fuel.gauge(99) == "F"

def test_other():
    assert fuel.gauge(45) == "45%"


