class User:
    def __init__(self, privelegies):
        self.login_attempts = False
        self.privelegies = privelegies

    def increment_login_attempts(self):
        self.login_attempts = True

    def reset_login_increment(self):
        self.login_attempts = False

    def show_login(self):
        print(self.login_attempts)





