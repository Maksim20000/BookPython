class Restaurant:
    def __init__(self):
        self.number_served = 0

    def get_number_served(self):
        print(f'{self.number_served} посетителей уже обслужены')

    def set_nuber_served(self, visitor_sered):
        self.number_served = visitor_sered

    def increment_served(self, served_visitors):
        self.number_served += served_visitors


myRestaurant = Restaurant()
myRestaurant.set_nuber_served(10)
myRestaurant.increment_served(4)

myRestaurant.get_number_served()


