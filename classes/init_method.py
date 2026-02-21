# 1. Класс Книга
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# 2. Класс Точка (координаты)
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# 3. Использование списков в __init__
class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

# 4. Класс с логикой в конструкторе
class User:
    def __init__(self, username):
        self.username = username.lower() # Авто-форматирование

# 5. Класс Банковский счет
class Account:
    def __init__(self, balance):
        self.balance = balance

b = Book("1984", "Оруэлл")
p = Point(10, 20)
t = Team("Разработчики")
u = User("ADMIN_Max")
a = Account(1000)
print("Все объекты успешно инициализированы")
