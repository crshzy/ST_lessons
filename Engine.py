from random import randint


class Engine(): # На кой черт скобки? ты ж ничего не наследуешь.

    def __init__(self):
        self.guessing_from = 1
        self.guessing_to = 10
        self.guessing_int = randint(self.guessing_from, self.guessing_to)
        self.start() # по хорошему, родительский класс не должен зависить от методов наследника. Подумай как сделать без этой зависимости

    def is_valid(self): # по неймингу: Наверное лучше is_numeric или можешь еще расширить валидацию на попадание введенного числа в диапазон
        try:
            self.user_number = int(self.user_number)
            return True
# лишняя строка
        except ValueError:
            print('Это разве число? Не похоже...')
            return False
















