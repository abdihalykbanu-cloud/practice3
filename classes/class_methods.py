class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    # 1. Метод изменения состояния
    def add_score(self, pts): self.score += pts
    # 2. Метод сброса
    def reset(self): self.score = 0
    # 3. Метод возврата строки
    def get_info(self): return f"{self.name}: {self.score}"
    # 4. Внутренний расчет
    def is_winner(self): return self.score > 100
    # 5. Метод приветствия другого игрока
    def greet(self, other): print(f"{self.name} жмет руку {other.name}")
