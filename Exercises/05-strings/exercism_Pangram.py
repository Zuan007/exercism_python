def is_pangram(sentence):
    """A pangram is a sentence using every letter
    
    :param sentence: str - sentence to be determined if it is a pangram or not
    :return: bool - answer to the question"""
    sentence = sentence.lower()
    unique_letters = set()

    for char in sentence:
        if 'a' <= char <= 'z':
            unique_letters.add(char)
    return len(unique_letters) == 26