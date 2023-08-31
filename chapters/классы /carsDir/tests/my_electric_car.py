from carsDir.electricCar import ElectricCar as EC

my_tesla = EC('Tesla', 'model s', 2019, 25)

print(my_tesla.get_descriptive_name())
my_tesla.battary.describe_battery()
my_tesla.battary.get_range()


