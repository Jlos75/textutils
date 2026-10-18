def word_count(text):
    """Count words separated by whitespace.

    Parameters
    ----------
    text : str
       Text whose words are counted.

    Returns
    -------
    int
       Number of words in the text.
    """
    words = text.split()
    return len(words)
