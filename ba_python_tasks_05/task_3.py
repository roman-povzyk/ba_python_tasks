our_list = []
second_list = []
i = 0

while i < 100:
    our_list.append(i+1)
    if our_list[i] % 7 == 0 and our_list[i] % 5 != 0:
        second_list.append(our_list[i])
    i += 1

print(second_list)
