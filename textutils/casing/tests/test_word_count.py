from textutils import word_count


def test_word_count():
    assert word_count("hello world") == 2


def test_word_count_empty_or_whitespace_only():
    assert word_count("") == 0
    assert word_count("   \t\n") == 0


def test_word_count_multiple_whitespace_separators():
    assert word_count("hello   world\tagain") == 3


def test_word_count_false():
    assert word_count("hello world") == 0
