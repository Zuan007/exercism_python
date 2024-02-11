"""Function that determines if a given string is a valid isbn."""
def is_valid(isbn):
    """An ISBN is used to validate book identification numbers
    
    :param isbn: str - the 10-digit identification number
    :return: bool - is the string an isbn or not?"""
    isbn = str(isbn.replace("-", ''))

    if len(isbn) != 10:
        return False

    total_sum = 0
    for i in range(len(isbn)):
        if isbn[i].isdigit():
            digit = int(isbn[i])
        elif i == 9 and isbn[i] == 'X':
            digit = 10
        else:
            return False

        total_sum += digit * (i + 1)

    return total_sum % 11 == 0