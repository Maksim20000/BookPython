with open('guest.txt', 'a') as file_object:
    name = input('Введите свое имя')
    file_object.write(name + '\n')
    print(f'Добро пожаловать {name}')
