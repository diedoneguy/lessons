'''
a = {
 'game':" gta"
}
a.update({'cinema':"hrre a"})
 print(a) 
a.update({'trainings' : "push ups"}) 
print(a)
 a.update({'cars': "Mersedes"})
 print(a)
 a.pop("game")
 print(a)

a = { 'cow', 'dog', 'fox', 'cat'
}
b = { 'horse', 'fox', 'cat', 'dog'}
a.difference(b) print(a)

what = input(" что делаем + , - , * , / ")
a = float(input(" введите первое число: ") )
b = float(input(" введите второе число: ") )
if what == "+":
	c = a + b
	print("результат: " + str (c))
elif what == "-":
	c = a - b
	print("результат: " + str (c)) 
elif what == "*":
	c = a * b
	print("результат: " + str (c))
elif what == "/":
	c = a / b
	print("результат: " + str (c))
else:
	print("неверная информация")

proffesion = {'Jacob':driverl


numbers = {'21':2,'21':3,'21':-23}
numbers.add('babl kwas')
print(numbers)
'''

print('добро пожаловать на наше кафе')

oficiant = str(input('вам дать меню?:'))

if oficiant == ('да'):
	print('что тогда закажите')
elif oficiant == ('нет'):
	print('хорощо')

menu = {
'Пицца': ['ПЕПЕРОНИ','ОХОТНИЧЬЯ','ГРИБНАЯ','С ОЛИВКАМИ']
}
print(menu)
menu.update({'Спагетти' : 1})
print(menu)
west = str(input('что выберите'))
if west == ('ПЕПЕРОНИ'):
	print('отличный выбор')
elif west == ('ОХОТНИЧЬЯ'):
	print('отличный выбор')
print(west + 'будет готова через 6 минут')
pony = str(input('закажите что нибудь попить?:'))
if pony == ('да'):
	print('принесем сейчас')
elif pony == ('нет'):
	print('ну ладно давай')
pop = {
'juices':['кола', 'фанта', 'пепси', 'спрайт']
}

print(pop)

vip = str(input('выберите что нибудь:'))
if vip == ('кола'):
	print('сию минуту')
elif vip == ('спрайт'):
	print('сейчас все будет')

