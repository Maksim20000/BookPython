'''Совенршает опрос и записысвает данные в базу данных'''

attempts = int(input('Сколько раз будет повторяться  программа?'))
while attempts > 0:
    answer = input('почему тебе нравится программирование?')
    with open('answer.txt', 'a') as file_name:
        file_name.write(answer + '\n')
    attempts = attempts - 1
