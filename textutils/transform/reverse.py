def reverse(text):
    """Return the text in reverse character order.

    Parameters
    ----------
    text : str
       Text to reverse.

    Returns
    -------
    str
       The characters of the text in reverse order.
    """
    reverse_text = ""
    for index in range(len(text)):
        reverse_text += text[len(text) - index - 1]
    return reverse_text
