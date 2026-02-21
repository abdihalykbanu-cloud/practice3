class Car:
    # 1. Переменная класса (общая)
    wheels = 4
    # 2. Счетчик созданных объектов
    count = 0
    
    def __init__(self, model):
        self.model = model # 3. Переменная экземпляра
        Car.count += 1
    # 4. Доступ к переменной класса через self
    def get_wheels(self): return self.wheels
    # 5. Изменение переменной класса для всех
    @classmethod
    def set_wheels(cls, n): cls.wheels = n
