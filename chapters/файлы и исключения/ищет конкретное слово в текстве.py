line = 'Row, row, row'

with open('../../file', 'r') as book:
    text = book.read()
    print(text.lower().count('mike'))


# print(line.lower().count('row'))
