from textutils import encrypt


def test_encrypt():
    assert encrypt("abc", 3) == "def"


def test_encrypt_wraps_alphabet_and_preserves_non_letters():
    assert encrypt("xyz XYZ! 123", 3) == "abc ABC! 123"

