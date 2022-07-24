from Engine import Engine


class FirstGame(Engine):

    def __init__(self):
        Engine.__init__(self)
        self.start()

    def start(self):
        self.user_number = input('Попробуй угадать число от 1 до 10: ')
        while True:
            if not self.is_valid():
                break

            if self.guessing_int == self.user_number:
                return print(f'Ты отгадал {self.guessing_int}! Молодец!')

            elif self.guessing_int > self.user_number:
                print('Загаданное число больше\n')
                break

            elif self.guessing_int < self.user_number:
                print('Загаданное число меньше\n')
                break

        if __name__ == '__main__':
            self.start()


FirstGame()
