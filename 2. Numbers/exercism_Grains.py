"""Code that shows how many number of grains are on a given square and whole chessboard"""
def square(number):
    """Calculate the number of grain from a given square
 
    :param number: int - what is the number of the chosen square?
    :return: int - how many grains are on the chosen square?
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)
def total():
    """Calculate the total number of grains in the chessboard
    
    :return: int - total number of grains"""
    return sum(2 ** i for i in range(64))