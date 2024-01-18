def square_root(number):
    if number <= 0:
        return "Only natural numbers!"

    approximate = number / 5

    for i in range(10):
        approximate = 0.5 * (approximate + number / approximate)

    return approximate

