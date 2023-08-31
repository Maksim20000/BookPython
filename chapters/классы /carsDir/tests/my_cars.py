from carsDir.car import Car
from carsDir.electricCar import ElectricCar as EC

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = EC('tesla', 'cybertruck', 2024, 50)
print(my_tesla.get_descriptive_name())
