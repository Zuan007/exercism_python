"""Function to get the square root of a natural number"""
def square_root(number):
    """Get the square root of a number without importing any math libraries

    :param number: int - number to get the square root of
    :return: int - square root of a number
    """
    if number <= 0:
        return "Only natural numbers!"

    approximate = number / 5

    for i in range(10):
        approximate = 0.5 * (approximate + number / approximate)

    return approximate

