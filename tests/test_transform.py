from textutils import reverse ,capitalize_words

def test_reverse():
   assert reverse("dodo") == "odod"
   
def test_capitalize_words():
   assert capitalize_words("Jean") == "JEAN"

#python -m pytest