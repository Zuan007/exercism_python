"""Function that determines if a given string is an isogram or not"""
def is_isogram(string):
    """An isogram is a word that contains all the letters of the alphabet without repetition
    
    :param string: str - word to be determined if isogram or not
    :return: bool - is the string an isogram or not?"""
    unique_letters = set()
    string = string.lower()
    
    for char in string:
        if 'a' <= char <= 'z':
            if char in unique_letters:
                return False
            else:
                unique_letters.add(char)
    return True