"""Function to determine whether a number is an armstrong number or not"""
def is_armstrong_number(number):
    """Check if a number is an Armstrong number.

    :param number: int - the number to check.
    :return: bool - True if the number is an Armstrong number, False otherwise.
    """
    str_num = str(number)
    length = len(str_num)
    sum = 0

    for digit in str_num:
        sum += int(digit) ** length
    return sum == number    