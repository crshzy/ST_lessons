from Engine import Engine


class SecondGame(Engine):

    def start(self):

        print(f'Загадай число от {self.guessing_from} до {self.guessing_to}!')

        while True:
            first_try = ((self.guessing_from + self.guessing_to) // 2)
            user_answer = input(f'Число больше, меньше или равно {first_try}? ')

            if user_answer == '=': # попробуй реализовать match case
                print(f'Это было легко..твое число {first_try}')
                return

            elif user_answer == '>':
                self.guessing_from = first_try
                break

            elif user_answer == '<':
                self.guessing_to = first_try
                break

            else:
                print('Не похоже на знаки равенства... введи >, < или =')



        self.start()


SecondGame()
