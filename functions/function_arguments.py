# 1. Позиционные аргументы
def power(base, exp):
    return base ** exp

# 2. Именованные аргументы (keyword arguments)
def describe_pet(animal, name):
    print(f"Пример 2: У меня есть {animal} по имени {name}")

# 3. Значения по умолчанию
def make_coffee(size='средний', sugar=2):
    print(f"Пример 3: Кофе {size}, сахара: {sugar} ложки")

# 4. Смешивание типов аргументов
def build_car(brand, model, color='белый'):
    print(f"Пример 4: {brand} {model}, цвет: {color}")

# 5. Изменяемые типы в аргументах (правильный подход)
def add_item(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket