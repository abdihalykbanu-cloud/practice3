# 1. Базовый вызов в __init__
class Parent:
    def __init__(self):
        self.attr = "родитель"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_attr = "ребенок"

# 2. Передача аргументов вверх
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Bike(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type

# 3. Вызов метода родителя (не конструктора)
class Worker:
    def work(self): return "Работаю"

class Manager(Worker):
    def work(self):
        return super().work() + " и руковожу"

# 4. Расширение функционала метода
class Logger:
    def log(self, msg): print(f"Log: {msg}")

class VerboseLogger(Logger):
    def log(self, msg):
        print("--- Start ---")
        super().log(msg)
        print("--- End ---")

# 5. Использование в цепочке (A -> B -> C)
class A:
    def test(self): print("A")

class B(A):
    def test(self):
        super().test()
        print("B")

print("Примеры super() подготовлены.")
