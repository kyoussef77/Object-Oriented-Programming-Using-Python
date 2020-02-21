from MathOperations.Addition import Addition


def Mean(data):
    num_values = len(data)
    total = 0
    for num in data:
        total = Addition.sum(total, num)
    return total / num_values
