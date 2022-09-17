import random


class Game:

    def __init__(self):
        self.arr = []
        self.line = 0
        self.row = 0
        self.line2 = 0
        self.row2 = 0
        self.player = 1
        self.num1 = 0
        self.num2 = 0
        self.exit_print = ''
        self.exit_print2 = ''
        self.win = 0

    def make_board(self):
        var = ''
        i = 0
        while i < 9:
            rand = random.randint(1, 9)
            var += str(rand)
            i += 1
            if len(var) == 3:
                self.arr.append(var)
                var = ''

    def show_board(self):
        i = 0
        while i < len(self.arr):
            print(self.arr[i])
            i += 1

    def get_step(self):
        print(f'Ход номер {self.player}')
        if self.player == 1:  # Условие, чтобы первый ход шёл без проверки
            self.line = int(input('Введите номер строки: '))
            self.row = int(input('Введите номер ряда: '))
        else:
            if self.player % 2 == 0:
                print(f'Ввести можно только ряд №{self.row2}')
                self.line = int(input('Введите номер строки: '))
                self.row = int(input('Введите номер ряда: '))

                if not self.row2 == self.row:  # Проверка, что игрок делает ход в нужном ряду
                    print('Неправильно введен ряд')
                    self.get_step()
            else:
                print(f'Ввести можно только строку №{self.line2}')
                self.line = int(input('Введите номер строки: '))
                self.row = int(input('Введите номер ряда: '))

                if not self.line2 == self.line:  # Проверка, что игрок делает ход в нужной строке
                    print('Неправильно введена строка')
                    self.get_step()

    def check_step(self):
        if self.player == 1:  # Условие, чтобы первый ход шёл без проверки
            self.step()
        else:
            if self.player % 2 == 0:
                if not (self.arr[self.line-1][self.row-1] == '-'):
                    print('good')
                    self.step()
                else:
                    self.exit_print = 'Нет хода'
                    print(self.exit_print)
                    self.player += 1
                    self.get_step()
            else:
                if not (self.arr[self.line-1][self.row-1] == '-'):
                    print('good')
                    self.step()
                else:
                    self.exit_print2 = 'Нет хода'
                    print(self.exit_print2)
                    self.player += 1
                    self.get_step()

    def step(self):
        if (0 < self.line < 4) and (0 < self.row < 4):
            if self.player % 2 == 0:
                self.line2 = self.line  # Переменная для сравнения значений в get_step
                self.num2 += int(self.arr[self.line-1][self.row-1:self.row])
                self.player += 1
                print(f'Second {self.num2}')
            else:
                self.row2 = self.row  # Переменная для сравнения значений в get_step
                self.num1 += int(self.arr[self.line-1][self.row-1:self.row])
                self.player += 1
                print(f'First {self.num1}')
            self.arr[self.line-1] = self.arr[self.line-1][:self.row - 1] + '-' + \
                self.arr[self.line-1][self.row:]  # Вычеркивает цифру
        else:
            if self.player == 1:  # Условие, чтобы первый ход шёл без проверки
                self.player = 1
            else:
                self.player -= 1
            print('Неправильное значение строки или ряда')
            self.get_step()

    def check_win(self):
        if self.arr == (['---'] * 3) or ((self.exit_print == 'Нет хода') and (self.exit_print2 == 'Нет хода')):
            self.win = 1
            if self.num1 > self.num2:
                print('Победил игрок №1')
            elif self.num1 == self.num2:
                print('Ничья')
            else:
                print('Победил игрок №2')

    def play(self):
        if not self.win == 1:
            self.get_step()
            self.check_step()
            self.show_board()
            self.check_win()
            self.play()
        else:
            print('Игра окончена')


game = Game()
game.make_board()
game.show_board()
game.play()
