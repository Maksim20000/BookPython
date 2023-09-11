def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            print(file.read())

    except FileNotFoundError:
        pass


read_file('doge')
