def word_count(text):
   """
   Count the parts of the text separated by spaces.
   
   Args:
      text (str): The input text
      
   Return: 
      int : the number of words
      
   """
   words = text.split(" ")
   return len(words)

