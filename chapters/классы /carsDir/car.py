""""Класс для представления автомобиля c бензином."""

class Car():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reader = 50
        self.gas = 10

    def update_odometr(self, milies):
        self.odometer_reader += milies

    def increment_odometr(self, miles):
        if miles > 0:
            self.odometer_reader += miles
        else:
            print('вы не можете добавлять отрицательные мили')
    def get_descriptive_name(self):
        lond_name = f'{self.brand} {self.model} {self.year}'
        return lond_name

    def fill_gas_tank(self):
        print(f'у этой машины расход {self.gas} литров на км')

    def read_odometer(self):
        print(f'Эта мвшина проехала {self.odometer_reader} милей')


