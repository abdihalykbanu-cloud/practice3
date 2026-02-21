# 1. Простая функция без аргументов
def say_hello():
    print("Пример 1: Привет из базовой функции!")

# 2. Функция с одним обязательным аргументом
def greet_person(name):
    print(f"Пример 2: Привет, {name}!")

# 3. Функция с несколькими аргументами
def show_info(city, weather):
    print(f"Пример 3: В городе {city} сейчас {weather}.")

# 4. Функция с циклом внутри
def repeat_msg(msg, times):
    print("Пример 4:")
    for _ in range(times):
        print(f" - {msg}")

# 5. Функция, вызывающая другую функцию
def main_task():
    print("Пример 5: Запуск основной задачи...")
    say_hello()