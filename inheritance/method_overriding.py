# 1. Базовый звук
class Animal:
    def sound(self): print("...")
# 2. Переопределение для кота
class Cat(Animal):
    def sound(self): print("Мяу")
# 3. Переопределение для собаки
class Dog(Animal):
    def sound(self): print("Гав")
# 4. Переопределение с логикой
class Bird(Animal):
    def sound(self): print("Чирик-чирик")
# 5. Список животных (полиморфизм)
for a in [Cat(), Dog(), Bird()]: a.sound()
