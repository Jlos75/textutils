from textutils import capitalize_words



def test_capitalize_words():
    assert capitalize_words("Jean") == "JEAN"


def test_capitalize_words_empty_and_mixed_case():
    assert capitalize_words("") == ""
    assert capitalize_words("Open Source!") == "OPEN SOURCE!"
