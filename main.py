class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reader = 50

    def update_odometr(self, milies):
        if self.odometer_reader <= milies:
            self.odometer_reader = milies
        else:
            print('Ты не можешь уменьшить пробег на своей машине')

    def increment_odometr(self, miles):
        if miles > 0:
            self.odometer_reader += miles
        else:
            print('вы не можете добавлять отрицательные мили')
    def get_descriptive_name(self):
        lond_name = f'{self.brand} {self.model} {self.year}'
        return lond_name

    def read_odometer(self):
        print(f'Эта мвшина проехала {self.odometer_reader} милей')

myCar = Car('Toyota', 'Prado', 2022)
myCar.update_odometr(100)
myCar.increment_odometr(-10)

myCar.read_odometer()
