"""Function to determine how many steps it takes to reach 1 given a number n"""
def steps(number):
    """Check how many steps is required to reach 1

    :param number: int - positive integer for the collatz conjecture
    :result: int - number of steps required
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
        
    num_steps = 0
    while number != 1:
        if (number % 2) == 0:
            number = number // 2
        else: 
            number = (number * 3) + 1
        num_steps = num_steps + 1
    return num_steps
            