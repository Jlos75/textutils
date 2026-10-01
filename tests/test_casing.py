from textutils import word_count, character_count

def test_word_count():
   assert word_count("hello world") == 2

def test_character_count():
   assert character_count("hello world") == 11