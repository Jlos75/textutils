from ._caesar import _shift_text


def encrypt(text, key):
    """Encrypt text using a Caesar cipher.

    Parameters
    ----------
    text : str
        Text to encrypt. Non-English letters are left unchanged.
    key : int
        Number of positions to shift English letters. Negative keys are valid.

    Returns
    -------
    str
        The encrypted text.
    """
    return _shift_text(text, key)
