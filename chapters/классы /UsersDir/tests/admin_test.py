from UsersDir.Admin import Admin

l = Admin('''
Разрешено добавлять сообщения
разрешено удалять пользователя 
разрешено банить людей
и тд
''')
l.privilegies.show_privelees()
