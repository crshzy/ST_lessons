import random


def game():
    print('Я хочу сыграть с тобой в игру ;]')
    guessing_number = guessing(random.randint(1, 10))
    print('Молодец! Ты угадал!!!')


def guessing(guessing_number):
    while True:
        try:
            user_number = int(input('Попробуй угадать число от 1 до 10: '))
            if guessing_number == user_number:
                return

            if guessing_number > user_number:
                print('Загаданное число больше\n')

            if guessing_number < user_number:
                print('Загаданное число меньше\n')

        except ValueError:
            print('Ты ввел не число, не надо так...')


if __name__ == '__main__':
    game()