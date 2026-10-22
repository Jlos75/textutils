from textutils import  decrypt_without_key


def test_decrypt_without_key():
    results = decrypt_without_key("Khoor Zruog")

    assert results[3] == "Hello World"


def test_decrypt_without_key_tests_all_keys():
    results = decrypt_without_key("abc")

    assert len(results) == 26
    assert set(results.keys()) == set(range(26))
