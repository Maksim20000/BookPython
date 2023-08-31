"""В этом файле представлен класс с рестараном"""

class Restaurant:
    def __init__(self, number_served):
        self.number_served = number_served

    def get_number_served(self):
        print(f'{self.number_served} посетителей уже обслужены')

    def set_nuber_served(self, visitor_sered):
        self.number_served = visitor_sered

    def increment_served(self, served_visitors):
        self.number_served += served_visitors

