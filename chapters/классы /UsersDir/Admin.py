''' Класс с админом'''

from UsersDir.user import User
class Admin(User):
    def __init__(self, privilegies):
        self.privilegies = Privileges(privilegies)

class Privileges():
    def __init__(self, privilegies):
        self.priviligies = privilegies

    def show_privelees(self):
        print(self.priviligies)
