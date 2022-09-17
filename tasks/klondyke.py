class Game:

    def __init__(self):
        self.arr = [" - - - - - - - - - -", " - - - - - - - - - -", " - - - - - - - - - -",
                    " - - - - - - - - - -",  " - - - - - - - - - -", " - - - - - - - - - -",
                    " - - - - - - - - - -",  " - - - - - - - - - -", " - - - 0 - - - - - -",
                    " - - - - - - - - - -"]
        self.player = 1
        self.line = 0
        self.row = 0

    def show_board(self):
        i = 0
        m = 10
        while i < len(self.arr):
            print(f'{m}  {self.arr[i]}')
            i += 1
            m -= 1
        print("    1 2 3 4 5 6 7 8 9 10")

    def get_step(self):
        print(f'Ход номер {self.player}')
        self.line = int(input('Введите номер строки: '))
        self.row = int(input('Введите номер ряда: '))
        self.player += 1

    def step(self):
        if (0 < self.line <= 10) and (0 < self.row <= 10):
            self.arr[-self.line] = self.arr[-self.line][:(self.row + (self.row - 1))] + '*' + \
                                   self.arr[-self.line][(self.row + self.row):]
        else:
            print('Неправильное значение строки или ряда')
            self.player -= 1
            self.get_step()

    # def check_loser(self):
    #     i = 0
    #     while i < 8:
    #         for j in self.arr[i]:
    #             x = self.arr[i][]
    #             if

    def play(self):
        self.get_step()
        self.step()
        self.show_board()


game = Game()
game.show_board()
game.play()
