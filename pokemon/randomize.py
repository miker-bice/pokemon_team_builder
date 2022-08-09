import random


def randomize(limit):
    random_result = random.sample(range(1, 100), limit)
    return random_result