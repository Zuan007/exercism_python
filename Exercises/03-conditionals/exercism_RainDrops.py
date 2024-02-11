"""Function to convert numbers to sound of rain drops"""
def convert(number):
    """Converts numbers that are factors of 3, 5, and 7 
    to sounds. If not a factor return the number.
    
    :param number: int - number to be converted
    :return: str - sound of rain drop or the digits of the number"""
    sound = ""
    if number % 3 == 0:
        sound += "Pling"

    if number % 5 == 0:
        sound += "Plang"

    if number % 7 == 0:
        sound += "Plong"

    if not number % 3 == 0 and not number % 5 == 0 and not number % 7 == 0:
        return str(number)
    
    return sound