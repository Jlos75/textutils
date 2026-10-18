from textutils import capitalize_words, reverse


def test_reverse():
    assert reverse("dodo") == "odod"


def test_reverse_empty_and_single_character():
    assert reverse("") == ""
    assert reverse("a") == "a"


def test_capitalize_words():
    assert capitalize_words("Jean") == "JEAN"


def test_capitalize_words_empty_and_mixed_case():
    assert capitalize_words("") == ""
    assert capitalize_words("Open Source!") == "OPEN SOURCE!"
