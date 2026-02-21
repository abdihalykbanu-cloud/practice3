# 1. Суммирование любого количества чисел (*args)
def sum_all(*args):
    return sum(args)

# 2. Печать списка имен через запятую
def print_names(*names):
    print("Список:", ", ".join(names))

# 3. Обработка настроек пользователя (**kwargs)
def set_settings(**kwargs):
    for key, value in kwargs.items():
        print(f"Настройка {key}: {value}")

# 4. Комбинирование args и kwargs
def pizza_order(size, *toppings, **details):
    print(f"Пицца {size}см. Добавки: {toppings}. Доп: {details}")

# 5. Передача словаря в функцию (распаковка)
def describe_pet(name, age):
    print(f"{name}у {age} лет")

pet_data = {"name": "Рекс", "age": 5}
describe_pet(**pet_data)
