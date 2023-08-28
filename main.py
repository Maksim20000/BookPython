class Restaurant:
    def __init__(self, restaurant_name, cuisine_name, first_name, last_name, phoneNumber, locate, code):
        self.code = code
        self.locate = locate
        self.phoneNumber = phoneNumber
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_name
        self.first_name = first_name
        self.last_name = last_name

    def describe_restaurant(self):
        print(f'Добрый день вы попали в {self.cuisine_name} кухню в ресторан под названием {self.restaurant_name}')

    def open_restaurant(self):
        print('Наш ресторан работает с 9 до 10')

    def usersInf(self):
        print(f'Добрый день {self.first_name} {self.last_name}')

    def greetUser(self):
        print(f'''ваш номер{self.phoneNumber}
Ваша локация{self.locate}
ваш код{self.code}
        ''')



tastyAndTochka = Restaurant('Вкусно и точка', 'фаст фуд', 'Максим', "Еловских", 79147989186, 'Vladivostok', 546)

tastyAndTochka.greetUser()


