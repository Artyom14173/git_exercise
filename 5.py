import random
n = int(input('сколько частей: '))
a = 1
b = (random.randint(0,9))
c = 7
for i in range(n):
    if b == a:
        b += 1
    elif b == c:
        b += 1
    else:
        b += 0

