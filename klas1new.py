a = int(input('чем сыграть: ')
def play (vibor, viborkompa, n):
    n = int(input('колво игр: '))
    for i in range (n):
        vibor = a
        viborkompa = (random.randint(1,3))
wins = 0
loses = 0
draws = 0
if vibor == viborkompa:
    print('draw')
    draws += 1
elif vibor == 1 and viborkompa == 2:
    print('win')
    wins += 1
elif vibor == 1 and viborkompa == 3:
    print('lose')
    loses += 1
elif vibor == 2 and viborkompa == 1:
    print('lose')
    loses += 1
elif vibor == 2 and viborkompa == 3:
    print('win')
    wins += 1
elif vibor == 3 and viborkompa == 1:
    print('win')
    wins += 1
elif vibor == 3 and viborkompa == 2:
    print('lose')
    loses += 1
else:
    print('error')
print(wins)
print(loses)
print(draws)
        
