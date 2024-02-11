def rotate(text, key):
    """A Rotational Cipher, also known as a Caesar Cipher, is a simple shift
    cipher that relies on transposing all the letters in the alphabet using
    a key integer
    
    :param text: str - text to be encrypted
    :param key: int - key integer
    :result: str - encrypted text"""
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    new_text = alphabet[key:] + alphabet[:key]
    translate = str.maketrans(alphabet + alphabet.upper(), new_text + new_text.upper())
    return text.translate(translate)