"""Fucntion for darts that gives points based on distance"""
def score(x, y):
    """Calculates the points using x and y

    :param x: int or float - distance in x-axis
    :param y: int or float - distance in y-axis
    :return: int or float - score calculated from distance
    """
    distance = ((x**2) + (y **2)) ** 0.5

    if distance <= 1:
        return 10
    if distance <= 5:
        return 5
    if distance <= 10:
        return 1
    return 0