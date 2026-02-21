# 1. Родительский класс
class Shape:
    def draw(self): print("Рисуем фигуру")
# 2. Простое наследование
class Circle(Shape): pass
# 3. Наследование с новым методом
class Square(Shape):
    def area(self): print("Считаем площадь")
# 4. Цепочка наследования (A->B->C)
class FastSquare(Square): pass
# 5. Проверка типа объекта
s = Square()
print(isinstance(s, Shape)) # True
