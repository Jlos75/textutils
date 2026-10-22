from textutils import decrypt
from textutils import encrypt


def test_decrypt_with_key():
    assert decrypt("def", 3) == "abc"


def test_decrypt_wraps_alphabet_and_preserves_non_letters():
    assert decrypt("abc ABC! 123", 3) == "xyz XYZ! 123"


def test_encrypt_then_decrypt():
    text = "Open Source 123!"
    encrypted = encrypt(text, 5)

    assert decrypt(encrypted, 5) == text


def test_empty_text_and_negative_key():
    assert encrypt("", 12) == ""
    assert decrypt("abc", -3) == "def"
