class Game:

    def __init__(self):
        self.arr = ["", " 123", " 456", " 789"]
        self.player = 1
        self.line = 0
        self.row = 0
        self.win = 0

    def show_board(self):
        i = 1
        while i < len(self.arr):
            print(self.arr[i])
            i += 1

    def get_step(self):
        if self.player == 1:
            self.line = int(input('Введите номер строки, куда поставить "х": '))
            self.row = int(input('Введите номер ряда, куда поставить "х": '))
            self.check_step()
        else:
            self.line = int(input('Введите номер строки, куда поставить "0": '))
            self.row = int(input('Введите номер ряда, куда поставить "0": '))
            self.check_step()

    def check_step(self):
        # Проверка для избежания повторного выбора того же места
        if self.arr[self.line][self.row] == 'x' or self.arr[self.line][self.row] == '0':
            print('Такой ход совершить нельзя')
            self.get_step()
        else:
            self.step()

    def step(self):
        if self.player == 1:
            self.arr[self.line] = self.arr[self.line][:self.row] + 'x' + self.arr[self.line][self.row+1:]
            self.player = 2
        else:
            self.arr[self.line] = self.arr[self.line][:self.row] + '0' + self.arr[self.line][self.row+1:]
            self.player = 1

    def check_win(self):
        # Проверка всех возможных вариантов выигрыша
        if self.arr[1] == ' xxx' or self.arr[1] == ' 000' or self.arr[2] == ' xxx' or self.arr[2] == ' 000' or \
                self.arr[3] == ' xxx' or self.arr[3] == ' 000' or (self.arr[1][1] == self.arr[2][2] == self.arr[3][3]) \
                or (self.arr[1][3] == self.arr[2][2] == self.arr[3][1]) or \
                (self.arr[1][1] == self.arr[2][1] == self.arr[3][1]) or \
                (self.arr[1][2] == self.arr[2][2] == self.arr[3][2]) \
                or (self.arr[1][3] == self.arr[2][3] == self.arr[3][3]):
            self.win = 1
            if self.player == 2:
                self.player = 1
            else:
                self.player = 2
            print(f'Победил игрок №{self.player}')

    def play(self):
        if not self.win == 1:
            self.get_step()
            self.show_board()
            self.check_win()
            self.play()
        else:
            print('Игра окончена')


game = Game()
game.show_board()
game.play()
