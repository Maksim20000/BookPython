"""Мороженое"""

from restaurantDir.restaurant import Restaurant
class IceCreamStand(Restaurant):
    def __init__(self, flavors, numbers_served):
        self.flavors = flavors
        super().__init__(numbers_served)

    def get_all_flavors(self):
        print(self.flavors)
