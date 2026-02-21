# 1. Возврат простого значения
def add(a, b):
    return a + b

# 2. Возврат нескольких значений (кортеж)
def get_min_max(numbers):
    return min(numbers), max(numbers)

# 3. Возврат словаря (структурированные данные)
def build_person(name, age):
    return {'name': name, 'age': age}

# 4. Ранний возврат (Early Return)
def check_adult(age):
    if age < 18:
        return "Доступ запрещен"
    return "Добро пожаловать"

# 5. Возврат результата логического выражения
def is_even(n):
    return n % 2 == 0

print(add(10, 5), get_min_max([1, 2, 3]), build_person("Ivan", 25), check_adult(20), is_even(4))
