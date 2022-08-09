import random


def randomize(limit):
    random_result = random.sample(range(1, 100), limit)
    return random_result


def single_randomize(original, data_id):
    new_random = random.randint(1, 100)
    index = original.index(data_id)
    original[index] = new_random
    return original