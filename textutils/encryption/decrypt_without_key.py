from .decrypt import decrypt


def decrypt_without_key(text):
    """Generate every possible Caesar decryption without knowing the key.

    The Caesar cipher has only 26 possible shifts, so every possible key
    can be tested.

    Parameters
    ----------
    text : str
        Text to decrypt with each possible key.

    Returns
    -------
    dict[int, str]
        Mapping from each key in the range 0 to 25 to its decrypted text.
    """
    results = {}

    for key in range(26):
        results[key] = decrypt(text, key)

    return results
