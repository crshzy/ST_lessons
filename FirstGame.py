from Engine import Engine


class FirstGame(Engine):

    def start(self):
        while True:
            self.user_number = int(input('Попробуй угадать число от 1 до 10: '))
            try:
                if self.guessing_int == self.user_number:
                    return print(f'Ты отгадал {self.guessing_int}! Молодец!')

                if self.guessing_int > self.user_number:
                    print('Загаданное число больше\n')

                if self.guessing_int < self.user_number:
                    print('Загаданное число меньше\n')

            except ValueError:
                print('Ты ввел не число, не надо так...')

        self.start()


FirstGame()

