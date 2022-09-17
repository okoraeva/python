class Game:

    def __init__(self):
        self.arr = [" x 0 x 0 x x x 0", " 0 0 x x x x x x", " 0 x 0 0 x x 0 0", " x 0 0 0 x x x x",
                    " 0 x 0 0 x 0 x x", " x 0 x 0 x x x 0", " x 0 x 0 x x x x", " 0 0 x x x x x 0"]
        self.row = "   a b c d e f g h"
        self.player = 1
        self.line = 0
        self.win = 0

    def show_board(self):
        i = 0
        m = 8
        while i < len(self.arr):
            print(f'{m} {self.arr[i]}')
            i += 1
            m -= 1
        print(self.row)

    def get_step(self):
        print(f'Ход номер {self.player}')
        self.line = input('Введите номер строки или ряда: ')
        if self.line.isdigit():  # Условие, чтобы можно было вводить и число, и букву
            self.line = int(self.line)
        self.player += 1

    def step(self):
        if isinstance(self.line, int):
            if 0 < self.line < 9:
                self.arr[-self.line] = ' 0 0 0 0 0 0 0 0'
            else:
                print('Неправильное значение строки или ряда')
                self.player -= 1
                self.get_step()
        elif isinstance(self.line, str):
            if 'a' <= self.line <= 'h':
                row = 0
                if self.line == 'd':
                    row = 7
                elif self.line == 'c':
                    row = 5
                elif self.line == 'b':
                    row = 3
                elif self.line == 'a':
                    row = 1
                elif self.line == 'e':
                    row = 9
                elif self.line == 'f':
                    row = 11
                elif self.line == 'g':
                    row = 13
                elif self.line == 'h':
                    row = 15
                i = 0
                while i < len(self.arr):
                    self.arr[i] = self.arr[i][:row] + '0' + self.arr[i][row+1:]
                    i += 1
            else:
                print('Неправильное значение строки или ряда')
                self.player -= 1
                self.get_step()

    def check_win(self):
        if self.arr == ([' 0 0 0 0 0 0 0 0'] * 8):
            if self.player % 2 == 0:
                self.player = 1
            else:
                self.player = 2
            print(f'Победил игрок №{self.player}')
            self.win = 1

    def play(self):
        if not self.win == 1:
            self.get_step()
            self.step()
            self.show_board()
            self.check_win()
            self.play()
        else:
            print('Игра окончена')


game = Game()
game.show_board()
game.play()
