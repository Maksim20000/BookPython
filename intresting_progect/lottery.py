import random

class Lottery():
    def __init__(self):
        self.series = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, "a", "b", "c", "d", "e"]
        self.myTicket = [1, 2, 3, 4]

    def random_choice(self):
        win = False
        quantity = 0

        while True:
            secret_combination = []
            for i in range(4):
                num = random.choice(self.series)
                secret_combination.append(num)

            print(secret_combination)

            if secret_combination == self.myTicket:
                print('Поздравляю вы выйграли миллион')
                print(quantity)
                break

            else:
                quantity += 1




lottery = Lottery()
lottery.random_choice()
