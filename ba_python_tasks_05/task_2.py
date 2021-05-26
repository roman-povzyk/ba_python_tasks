import random

list_1, list_2 = [], []
i = 0

while i < 10:
    list_1.append(random.randint(1, 10))
    list_2.append(random.randint(1, 10))
    i += 1

set_3 = set(list_1) & set(list_2)
list_3 = list(set_3)

print(list_3)
