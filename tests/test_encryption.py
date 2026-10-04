from textutils import decrypt, encrypt


def test_encrypt():
    assert encrypt("abc", 3) == "def"


def test_decrypt():
    assert decrypt("def", 3) == "abc"


def test_encrypt_preserves_case():
    assert encrypt("AbC", 1) == "BcD"


def test_encrypt_preserves_non_letters():
    assert encrypt("hello world!", 3) == "khoor zruog!"


def test_encrypt_then_decrypt():
    text = "Open Source 123!"
    encrypted = encrypt(text, 5)

    assert decrypt(encrypted, 5) == text


def test_default_key():
    encrypted = encrypt("abc")
    assert encrypted == "def"
    assert decrypt(encrypted) == "abc"