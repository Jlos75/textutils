from textutils import decrypt, decrypt_without_key, encrypt


def test_encrypt():
    assert encrypt("abc", 3) == "def"


def test_encrypt_wraps_alphabet_and_preserves_non_letters():
    assert encrypt("xyz XYZ! 123", 3) == "abc ABC! 123"


def test_decrypt_with_key():
    assert decrypt("def", 3) == "abc"


def test_decrypt_wraps_alphabet_and_preserves_non_letters():
    assert decrypt("abc ABC! 123", 3) == "xyz XYZ! 123"


def test_decrypt_without_key():
    results = decrypt_without_key("Khoor Zruog")

    assert results[3] == "Hello World"


def test_decrypt_without_key_tests_all_keys():
    results = decrypt_without_key("abc")

    assert len(results) == 26
    assert set(results.keys()) == set(range(26))


def test_encrypt_then_decrypt():
    text = "Open Source 123!"
    encrypted = encrypt(text, 5)

    assert decrypt(encrypted, 5) == text


def test_empty_text_and_negative_key():
    assert encrypt("", 12) == ""
    assert decrypt("abc", -3) == "def"
