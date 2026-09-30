

def reverse(text):
   reverse_text = ""
   for i in range(len(text)):
      reverse_text += text[len(text)-i-1]
   return reverse_text

   
def capitalize_words(text):
   return text.upper()
