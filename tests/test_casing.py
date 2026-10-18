from textutils import character_count, word_count


def test_word_count():
    assert word_count("hello world") == 2


def test_word_count_empty_or_whitespace_only():
    assert word_count("") == 0
    assert word_count("   \t\n") == 0


def test_word_count_multiple_whitespace_separators():
    assert word_count("hello   world\tagain") == 3


def test_character_count():
    assert character_count("hello world") == 11


def test_character_count_empty():
    assert character_count("") == 0
