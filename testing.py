import random

original = [1, 2, 3, 4, 5, 6]
print(original)
data_id = 4

new_random = random.randint(1, 100)

index = original.index(data_id)
print(index)

original[index] = new_random
print(original)


