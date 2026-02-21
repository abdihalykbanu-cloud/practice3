# 1. Сортировка по длине слова
fruits = ["banana", "apple", "kiwi", "cherry"]
s1 = sorted(fruits, key=lambda x: len(x))
# 2. Сортировка списка цен (от дешевых)
prices = [("milk", 100), ("bread", 50), ("meat", 500)]
s2 = sorted(prices, key=lambda x: x[1])
# 3. Сортировка по последней букве
s3 = sorted(fruits, key=lambda x: x[-1])
# 4. Обратная сортировка по числам
s4 = sorted([1, 10, 5, 2], key=lambda x: -x)
# 5. Сортировка словаря по значениям
d = {'a': 10, 'b': 1, 'c': 5}
s5 = sorted(d.items(), key=lambda x: x[1])
