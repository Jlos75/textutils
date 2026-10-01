

def reverse(text):
   """Return the text in reverse order."""
   reverse_text = ""
   for i in range(len(text)):
      reverse_text += text[len(text)-i-1]
   return reverse_text

   
def capitalize_words(text):
   """Convert all characters in the text to uppercase."""
   return text.upper()
