nums = [1, -5, 10, 0, 4, -2, 7]
# 1. Только положительные
pos = list(filter(lambda x: x > 0, nums))
# 2. Слова длиннее 5 букв
words = ["apple", "hi", "python", "code"]
long_w = list(filter(lambda s: len(s) > 5, words))
# 3. Поиск четных чисел
evens = list(filter(lambda x: x % 2 == 0, nums))
# 4. Удаление None из списка
data = [1, None, 2, None, 3]
clean = list(filter(lambda x: x is not None, data))
# 5. Числа, делящиеся на 3 и 5
nums2 = [15, 3, 5, 30, 7]
divisible = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, nums2))
