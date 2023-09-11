fileName = 'alice.txt'
try:
    with open(fileName, encoding='utf-8') as f:
        print(f.read())

except FileNotFoundError:
    print('Файла в каталоге нет')
