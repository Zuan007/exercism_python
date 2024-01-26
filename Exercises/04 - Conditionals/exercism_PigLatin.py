"""Function that translates English to Pig Latin"""
def translate(text):
    """Translate to Pig Latin using 4 rules
    
    :param text: str - English word to be translated to Pig Latin
    :return: str - Translated English Word"""

    # Rule 1: if a word begins with a vowel sound, add -ay at the end
    vowels = 'aeiou'
    if any(text.lower().startswith(vowel) for vowel in vowels):
        return text + 'ay'
    if text.startswith('xr') or text.startswith('yt'):
        return text + 'ay'

    # Rule 2: if a word begins with a consonant sound, move it to the end of the word and add -ay
    for i, char in enumerate(text.lower()):
        if char in vowels:
            return text[i:] + text[:i] + 'ay'
        
    # Rule 3: if a word starts with a consonant sound followed by qu, move it to the end and add
    if text.lower().startswith("qu"):
        return text[:] + 'quay'
    
    # Rule 4: if a word contains 'y' after a consonant cluster, it makes a vowel sound
    if text[0] == 'y' or text[1] == 'y':
        return 'y' + text[0] + 'ay'
    
print(translate('queen'))
print(translate('square'))