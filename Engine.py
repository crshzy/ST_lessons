from random import randint


class Engine():

    def __init__(self):
        self.guessing_from = 1
        self.guessing_to = 100
        self.guessing_int = randint(self.guessing_from, self.guessing_to)
        self.start()









