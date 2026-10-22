from textutils import  reverse


def test_reverse():
    assert reverse("dodo") == "odod"


def test_reverse_empty_and_single_character():
    assert reverse("") == ""
    assert reverse("a") == "a"


