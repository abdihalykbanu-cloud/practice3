# 1. Преобразование чисел в строки
nums = [1, 2, 3]
str_nums = list(map(lambda x: f"Число {x}", nums))

# 2. Возведение в квадрат
squares = list(map(lambda x: x**2, [4, 5, 6]))

# 3. Приведение имен к верхнему регистру
names = ["ivan", "mary", "alex"]
caps = list(map(lambda n: n.upper(), names))

# 4. Вычисление длины слов
lengths = list(map(lambda s: len(s), ["apple", "banana", "cherry"]))

# 5. Извлечение первого элемента из кортежей
pairs = [(1, 'a'), (2, 'b')]
firsts = list(map(lambda p: p[0], pairs))

print(str_nums, squares, caps, lengths, firsts, sep="\n")
