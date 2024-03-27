from twttr import shorten

def test_vowel_lower():
    assert shorten("paiueop") == "pp"

def test_vowel_upper():
    assert shorten("PAIUEOP") == "PP"

def test_numbers():
    assert shorten("p0123456789p") == "p0123456789p"

def test_punct():
    assert shorten("pa,i.u?epo") == "p,.?p"
