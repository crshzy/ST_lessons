from random import randint


class Engine():

    def __init__(self):
        self.guessing_from = 1
        self.guessing_to = 10
        self.guessing_int = randint(self.guessing_from, self.guessing_to)
        self.start()

    def is_valid(self):
        try:
            self.user_number = int(self.user_number)
            return True

        except ValueError:
            print('Это разве число? Не похоже...')
            return False
















