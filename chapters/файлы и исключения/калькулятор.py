def sum_two_num(a, b):
    try:
        print(a + b)
    except ValueError:
        print('введи число, а не букву')

while True:
    try:
        a = input('Введи первое число')
        b = input('Введи второе число')
        sum_two_num(int(a), int(b))

    except ValueError:
        print('Введи число')
