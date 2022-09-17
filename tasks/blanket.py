class Game:

    def __init__(self):
        self.arr = ['', ' * * * * *', ' * * * * *', ' * * * * *', ' * * * * *']
        self.line = 0
        self.row = 0
        self.player = 1
        self.counter = 0
        self.sign = ''

    def show_board(self):
        i = 1
        num = 1
        while i < len(self.arr):
            print(f'{num}  {self.arr[i]}')
            num += 1
            i += 1
        print('    1 2 3 4 5')

    def get_step(self):
        print(f'Ход номер {self.player}')
        self.line = int(input('Введите номер строки: '))
        self.row = int(input('Введите номер ряда: '))
        self.sign = input('Введите символ: ')
        self.player += 1

    def step(self):
        if (0 < self.line <= 4) and (0 < self.row <= 5):
            self.arr[self.line] = self.arr[self.line][:(self.row + (self.row - 1))] + self.sign + \
                                   self.arr[self.line][(self.row + self.row):]
        else:
            print('Неправильное значение строки или ряда')
            self.player -= 1
            self.get_step()

    def count_points(self):
        for i in self.arr:
            for j in i:
                compare = j
                #if (self.line - 1) < 0:
                if compare == self.arr[self.line][self.row+1]:
                    self.counter += 1
                if compare == self.arr[self.line][self.row-1]:
                    self.counter += 1
                if compare == self.arr[self.line+1][self.row]:
                    self.counter += 1
                if compare == self.arr[self.line+1][self.row-1]:
                    self.counter += 1
                if compare == self.arr[self.line+1][self.row+1]:
                    self.counter += 1
        print(self.counter)


    def play(self):
        self.get_step()
        self.step()
        self.count_points()
        self.show_board()
        self.play()


game = Game()
game.show_board()
game.play()
