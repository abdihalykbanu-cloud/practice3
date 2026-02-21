# 1. Способность летать
class Flyable:
    def fly(self): print("Летит")
# 2. Способность плавать
class Swimmable:
    def swim(self): print("Плывет")
# 3. Класс Утка (летает и плавает)
class Duck(Flyable, Swimmable): pass
# 4. Класс Самолет-амфибия
class Seaplane(Flyable, Swimmable): pass
# 5. Проверка порядка вызова методов (MRO)
print(Duck.mro())
