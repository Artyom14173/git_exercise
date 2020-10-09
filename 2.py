Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = int(input("Введите число: "))
Введите число: 5
>>> if -10 >= x < 10:
	print(x - 5)
    else: print(x - 10)
    
SyntaxError: unindent does not match any outer indentation level
>>> #2е задание
>>> months = {1:'январь', 2:'февраль', 3:'март', 4:'апрель', 5:'май', 6:'июнь', 7:'июль', 8:'август', 9:'сентябрь', 10:'октябрь', 11:'ноябрь', 12:'декабрь'}
>>> def month(n):
	print(months[n])
    while True:
	    
SyntaxError: unindent does not match any outer indentation level
>>> while True:
	try:
		month (int(input('Введите номер месяца: ')))
	except:
		break
#3е задание

>>> storoni = {11:'север', 12:'восток', 13:'юг', 14:'запад'}
>>> def storona(n):
	print(storoni[n])

	
>>> while True:
	try:
		storona (int(input('Введите номер стороны света: ')))
	except:
		break