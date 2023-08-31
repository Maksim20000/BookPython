""""Класс для представления автомобиля c электродвигателем."""
from carsDir.car import Car
class ElectricCar(Car):
    def __init__(self, brand, model, year, battary_size):
        super().__init__(brand, model, year)
        self.battary = Battary(battary_size)
    def fill_gas_tank(self):
        print(' уэтой машине нет доступа к бензину')



class Battary():
    def __init__(self, battary_size):
        self.battary_size = battary_size

    def update_battary(self, battery_added):
        self.battary_size += battery_added
    def describe_battery(self):
        print(f'состояние вашего аккумулятора находится на значении {self.battary_size}')

    def get_range(self):
        if self.battary_size == 75:
            range = 260
        elif self.battary_size == 100:
            range = 315
        elif self.battary_size == 50:
            range = 100
        elif self.battary_size == 25:
            range = 50

        print(f'Запаса хода вам еще хватит на {range} миль')
