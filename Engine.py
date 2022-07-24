from random import randint


class Engine:

    def __init__(self):
        self.guessing_from = 1
        self.guessing_to = 10
        self.guessing_int = randint(self.guessing_from, self.guessing_to)
        self.user_number = 0

    def is_valid(self):
        try:
            self.user_number = int(self.user_number)
            if int(self.user_number) > self.guessing_to:
                print(f'{self.user_number} слишком большое число')
                return False
            elif int(self.user_number) < self.guessing_from:
                print(f'{self.user_number} слишком маленькое число')
                return False
            return True
        except ValueError:
            print('Это разве число? Не похоже...')
            return False
















