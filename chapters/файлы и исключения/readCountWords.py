'''Алгоритм который считает сколько слов в тексте'''

def count_words(fileName):
    '''функция подчсета слов в тексте'''
    try:
        with open(fileName, encoding='utf-8') as f:
            content = f.read()

    except FileNotFoundError:
        with open('../../exeptions.txt', 'a') as exeptions:
            exeptions.write(fileName)
        pass

    else:
        words = content.split()
        num_words = len(words)
        print(num_words)

fileNames = ['alice.txt', 'second', 'miak', 'fjfj']
for fileName in fileNames:
    count_words(fileName)

