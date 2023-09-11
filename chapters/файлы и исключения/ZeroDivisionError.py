print('напиши мне 2 числа')
print('Нажми q чтобы закончить')

while True:
    first_number = input('Введи первое число')
    if first_number == 'q':
        break

    second_number = input('введи второе число')
    if second_number == 'q':
        break

    try:
        result = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('ты не можешь делить на ноль')
    except ValueError:
        print('не корректное число или слово')
    else:
        print(result)
