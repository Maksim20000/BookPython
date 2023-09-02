'''В этом файле я перебираю все цифры числа пи и проверяю совпала ли моя дата рождения с ним'''

with open('pi_digits') as file_object:
    lines = file_object.read()

pi = ''
for line in lines:
    pi += line.rstrip()
while True:
    year_birthda = input('Др')
    if year_birthda in pi:
        print('у тебя есть др в числе pi')
    else:
        print('нет')
