from carsDir.car import Car

my_new_car = Car('Audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometr(1000)
my_new_car.read_odometer()
