# The 'sys.path' list is initialized from the PYTHONPATH environment variable.
# Is it possible to change it from within Python? If so,
# does it affect where Python looks for module files?
# Run some interactive tests to find it out.


import sys

# переглядаємо всі шляхи
for i in range(len(sys.path)):
    print(sys.path[i])

# перший шлях ставимо на останнє місце
a = sys.path[0]
sys.path.remove(sys.path[0])
sys.path.append(a)
print()

# переглядаємо поточний перелік шляхів
for i in range(len(sys.path)):
    print(sys.path[i])
