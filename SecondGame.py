from Engine import Engine


class SecondGame(Engine):

    def __init__(self):
        Engine.__init__(self)
        self.start()

    def start(self):
        print(f'Загадай число от {self.guessing_from} до {self.guessing_to}!')
        while True:
            first_try = ((self.guessing_from + self.guessing_to) // 2)
            user_answer = input(f'Число больше, меньше или равно {first_try}? ')

            match user_answer:
                case '=':
                    return print(f'Это было легко..твое число {first_try}')
                case '>':
                    self.guessing_from = first_try
                case '<':
                    self.guessing_to = first_try
                case _:
                    print('Не похоже на знаки равенства... введи >, < или =')

        if __name__ == '__main__':
            self.start()


SecondGame()
