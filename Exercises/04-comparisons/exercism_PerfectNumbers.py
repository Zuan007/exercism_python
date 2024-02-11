def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    divisor_sum = sum([i for i in range(1,number) if number % i == 0])

    if divisor_sum == number:
        return "perfect"
    if divisor_sum > number:
        return "abundant"
    return "deficient"