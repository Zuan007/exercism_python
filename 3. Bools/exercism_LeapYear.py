"""Function to determine if it is a leap year."""
def leap_year(year):
    """Determine if year is a leap year
    
    :param year: int - year that needs to be determined if leap year or not
    :return: bool - return True if it is a leap year
    
    """

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
