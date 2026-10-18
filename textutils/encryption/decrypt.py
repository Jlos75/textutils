from ._caesar import _shift_text


def decrypt(text, key):
    """Decrypt text encrypted with a Caesar cipher.

    Parameters
    ----------
    text : str
        Text to decrypt. Non-English letters are left unchanged.
    key : int
        Number of positions used during encryption. Negative keys are valid.

    Returns
    -------
    str
        The decrypted text.
    """
    return _shift_text(text, -key)
