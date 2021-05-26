import random

i = 0
our_list = []

while i < 10:
    our_list.append(random.randint(1, 100))
    i += 1

print(f'Найбільше число у списку — {max(our_list)}')
