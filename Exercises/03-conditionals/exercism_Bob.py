"""Function to determine what Bob will reply to someone"""

def response(hey_bob):
    """Basic response function for Bob.
    
    :param hey_bob: str - message you want to say to Bob
    :return: str - Bob's reply to you
    """

    if hey_bob.isspace() or not hey_bob:
        return "Fine. Be that way!"
    
    if hey_bob.isupper():
        if hey_bob.endswith("?"):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    
    if hey_bob.strip().endswith("?"):
        return "Sure."
    return "Whatever."