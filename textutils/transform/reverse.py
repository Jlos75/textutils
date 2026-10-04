def reverse(text):
   """
   Return the text in reverse order.
   
   Args:
      text (str): The input text
      
   Return: 
      str : The reversed text
      
   """
   reverse_text = ""
   for i in range(len(text)):
      reverse_text += text[len(text)-i-1]
   return reverse_text
