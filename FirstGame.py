from Engine import Engine


class FirstGame(Engine):

    def start(self):
        self.user_number = input('Попробуй угадать число от 1 до 10: ') # работаешь с незадекларированной переменной
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

        self.start() #Используешь неявное зацикливание, подумай, как сделать более явно (не ошибка)


FirstGame()
