from Engine import Engine


class SecondGame(Engine):

    def start(self):

        while True:
            first_try = ((self.guessing_from + self.guessing_to) // 2)
            user_answer = input(f'Число больше, меньше или равно {first_try}? ')

            if user_answer == '=':
                print(f'Это было легко..твое число {first_try}')
                break

            elif user_answer == '>':
                self.guessing_from = first_try
                break

            elif user_answer == '<':
                self.guessing_to = first_try
                break

            else:
                print('Чеее??')
                break


        self.start()


SecondGame()
