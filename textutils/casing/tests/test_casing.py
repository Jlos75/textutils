from textutils import character_count


def test_character_count():
    assert character_count("hello world") == 11


def test_character_count_empty():
    assert character_count("") == 0

#vérifiere caractere spécieau