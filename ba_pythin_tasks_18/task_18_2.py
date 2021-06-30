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
