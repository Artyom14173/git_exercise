import random
n = int(input('колво игр: '))
побед = 0
поражений = 0
ничьих = 0
for i in range (n):
    a = int(input('чем сыграть: '))
    b = (random.randint(1, 3))
    if a == b:
        print('ничья')
        ничьих += 1
    elif a ==1 and b == 2:
        print('победа')
        побед += 1
    elif a == 1 and b == 3:
        print('поражение')
        поражений += 1
    elif a == 2 and b == 1:
        print('поражение')
        поражений += 1
    elif a == 2 and b == 3:
        print('победа')
        побед += 1
    elif a == 3 and b == 1:
        print('победа')
        побед += 1
    elif a == 3 and b == 2:
        print('поражение')
        поражений += 1
    else:
        print('WTF')
print(побед)
print(поражений)
print(ничьих)
