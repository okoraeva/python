class Game:

    def __init__(self):
        self.arr = [" R N B Q K B N R", " p p p p p p p p", " . . . . . . . .", " . . . . . . . .",
                    " . . . . . . . .", " . . . . . . . .", " p p p p p p p p", " R N B Q K B N R"]
        self.player = 1
        self.line = 0
        self.row = ''
        self.line2 = 0
        self.row2 = ''
        self.counter = 0

    def show_board(self):
        letter_row = "   A B C D E F G H"
        i = 0
        m = 8
        print(letter_row)
        print('   ---------------')
        while i < len(self.arr):
            print(f'{m} {self.arr[i]}  {m}')
            i += 1
            m -= 1
        print('   ---------------')
        print(letter_row)

    def get_step(self):
        print(f'Ход номер {self.player}')
        if self.player % 2 == 0:
            print('Ходят чёрные')
        else:
            print('Ходят белые')
        user_input = list(input('Введите ход: '))
        if ' ' in user_input:
            user_input.remove(' ')
        if '-' in user_input:
            user_input.remove('-')
        print(user_input)
        if len(user_input) == 4:
            self.line = int(user_input[1])
            self.row = user_input[0]
            self.line2 = int(user_input[3])
            self.row2 = user_input[2]
        elif len(user_input) == 5 and user_input[0] in 'prnbqkPRNBQK':
            self.line = int(user_input[2])
            self.row = user_input[1]
            self.line2 = int(user_input[4])
            self.row2 = user_input[3]
        else:
            self.get_step()
            self.step()
        self.row = self.check_index(self.row)
        self.row2 = self.check_index(self.row2)
        self.player += 1

    def check_index(self, x):
        row_position = 0
        x = x.lower()
        if x == 'a':
            row_position = 1
        elif x == 'b':
            row_position = 3
        elif x == 'c':
            row_position = 5
        elif x == 'd':
            row_position = 7
        elif x == 'e':
            row_position = 9
        elif x == 'f':
            row_position = 11
        elif x == 'g':
            row_position = 13
        elif x == 'h':
            row_position = 15
        else:
            print('Неправильно выбран ряд')
            self.player -= 1
            self.get_step()
        return row_position

    def check_position(self, x, y, x2, y2):
        # Проверка на правильночть ввода строки
        if x not in range(1, 9) or x2 not in range(1, 9):
            print('Неправильно выбрана строка')
            return 0
        # Проверка, что выбрано не пустое поле
        if self.arr[-x][y] == '.':
            print('Вы выбрали пустое поле, попробуйте ещё!')
            return 0
        # Проверка на правильность ввода ряда
        if self.arr[-x][y] in 'prnbqk' and self.arr[-x2][y2] not in 'prnbqk':
            return 1
        elif self.arr[-x][y] in 'PRNBQK' and self.arr[-x2][y2] not in 'PRNBQK':
            return 1
        else:
            print('Здесь стоит Ваша фигура!')
            return 0

    def check_pawn(self):
        if 'p' in self.arr[7]:
            figure = input('Выберите новую фигуру(r, n, b, q): ')
            while figure not in 'rnbqRNBQ':
                print('Вы ввели неправильную фигуру!')
                figure = input('Выберите новую фигуру(r, n, b, q): ')
            self.arr[-self.line2] = self.arr[-self.line2][:self.row2] + figure + self.arr[-self.line2][self.row2+1:]
        if 'P' in self.arr[0]:
            figure = input('Выберите новую фигуру(R, N, B, Q): ')
            while figure not in 'rnbqRNBQ':
                print('Вы ввели неправильную фигуру!')
                figure = input('Выберите новую фигуру(R, N, B, Q): ')
            self.arr[-self.line2] = self.arr[-self.line2][:self.row2] + figure + self.arr[-self.line2][self.row2+1:]
        if 'p' in self.arr[4] and self.line == 2 and self.line2 == 4 and (self.arr[4].index('p') - self.row2 == 2 or self.arr[4].index('p') - self.row2 == -2):
            self.arr[-self.line2] = self.arr[-self.line2][:self.row2] + '.' + self.arr[-self.line2][self.row2+1:]
            self.arr[-self.line2+1] = self.arr[-self.line2+1][:self.row2] + 'p' + self.arr[-self.line2+1][self.row2+1:]
            self.arr[4] = self.arr[4][:(self.arr[4].index('p'))] + '.' + self.arr[4][(self.arr[4].index('p'))+1:]
        if 'P' in self.arr[3] and self.line == 7 and self.line2 == 5 and (self.arr[3].index('P') - self.row2 == 2 or self.arr[3].index('P') - self.row2 == -2):
            self.arr[-self.line2] = self.arr[-self.line2][:self.row2] + '.' + self.arr[-self.line2][self.row2+1:]
            self.arr[-self.line2-1] = self.arr[-self.line2-1][:self.row2] + 'P' + self.arr[-self.line2-1][self.row2+1:]
            self.arr[3] = self.arr[3][:(self.arr[3].index('P'))] + '.' + self.arr[3][(self.arr[3].index('P'))+1:]

    def check_rook(self):
        if 'R . . . K' in self.arr[7] or 'K . . R' in self.arr[7]:
            if self.line2 == 1 and self.row2 == 5:
                self.arr[-self.line] = self.arr[-self.line][:9] + '.' + self.arr[-self.line][10:]
                self.arr[-self.line] = self.arr[-self.line][:self.row2] + 'K' + self.arr[-self.line][self.row2+1:]
                self.arr[-self.line] = self.arr[-self.line][:self.row2+2] + 'R' + self.arr[-self.line][self.row2+3:]
                self.arr[-self.line] = self.arr[-self.line][:1] + '.' + self.arr[-self.line][2:]
                return 1
            elif self.line2 == 1 and self.row2 == 13:
                self.arr[-self.line] = self.arr[-self.line][:9] + '.' + self.arr[-self.line][10:]
                self.arr[-self.line2] = self.arr[-self.line2][:self.row2] + 'K' + self.arr[-self.line2][self.row2+1:]
                self.arr[-self.line2] = self.arr[-self.line2][:11] + 'R' + self.arr[-self.line2][12:]
                self.arr[-self.line2] = self.arr[-self.line2][:15] + '.' + self.arr[-self.line2][16:]
                return 1
            else:
                return 0
        if 'r . . . k' in self.arr[0] or 'k . . r' in self.arr[0]:
            if self.line2 == 8 and self.row2 == 5:
                self.arr[-self.line] = self.arr[-self.line][:9] + '.' + self.arr[-self.line][10:]
                self.arr[-self.line] = self.arr[-self.line][:self.row2] + 'k' + self.arr[-self.line][self.row2+1:]
                self.arr[-self.line] = self.arr[-self.line][:self.row2+2] + 'r' + self.arr[-self.line][self.row2+3:]
                self.arr[-self.line] = self.arr[-self.line][:1] + '.' + self.arr[-self.line][2:]
                return 1
            elif self.line2 == 8 and self.row2 == 13:
                self.arr[-self.line] = self.arr[-self.line][:9] + '.' + self.arr[-self.line][10:]
                self.arr[-self.line2] = self.arr[-self.line2][:self.row2] + 'k' + self.arr[-self.line2][self.row2+1:]
                self.arr[-self.line2] = self.arr[-self.line2][:11] + 'r' + self.arr[-self.line2][12:]
                self.arr[-self.line2] = self.arr[-self.line2][:15] + '.' + self.arr[-self.line2][16:]
                return 1
            else:
                return 0

    def check_step(self, fig):
        if fig == 'p' or fig == 'P':
            if self.row2 == self.row or ((self.row2 - self.row == 2 or self.row2 - self.row == -2) and (not self.arr[-self.line2][self.row2] == '.')):
                if fig == 'p':
                    if (self.line == 7 and 4 < self.line2 < 7) or (self.line2 - self.line == -1):
                        return 1
                    else:
                        return 0
                if fig == 'P':
                    if (self.line == 2 and 2 < self.line2 < 5) or (self.line2 - self.line == 1):
                        return 1
                    else:
                        return 0
            else:
                return 0
        if fig == 'r' or fig == 'R':
            if self.line == self.line2:
                if self.row2 > self.row:
                    i = self.row+1
                    while i < self.row2:
                        if self.arr[-self.line][i] == ' ' or self.arr[-self.line][i] == '.':
                            i += 1
                        else:
                            return 0
                else:
                    i = self.row-1
                    while i > self.row2:
                        if self.arr[-self.line][i] == ' ' or self.arr[-self.line][i] == '.':
                            i -= 1
                        else:
                            return 0
                return 1
            elif self.row == self.row2:
                if self.line < self.line2:
                    i = self.line+1
                    while i < self.line2:
                        if self.arr[-i][self.row] == ' ' or self.arr[-i][self.row] == '.':
                            i += 1
                        else:
                            return 0
                else:
                    i = self.line-1
                    while i > self.line2:
                        if self.arr[-i][self.row] == ' ' or self.arr[-i][self.row] == '.':
                            i -= 1
                        else:
                            return 0
                return 1
        if fig == 'n' or fig == 'N':
            if (self.line2 - self.line == 2 or self.line2 - self.line == -2) and (self.row2 - self.row == 2 or self.row2 - self.row == -2):
                return 1
            elif (self.line2 - self.line == 1 or self.line2 - self.line == -1) and (self.row2 - self.row == 4 or self.row2 - self.row == -4):
                return 1
            else:
                return 0
        if fig == 'b' or fig == 'B':
            if self.line > self.line2:
                x = self.line-1
                y = 1
                while x > self.line2:
                    if self.row2 > self.row and self.arr[-x][self.row+(y*2)] != '.':
                        return 0
                    elif self.row2 < self.row and self.arr[-x][self.row-(y*2)] != '.':
                        return 0
                    x -= 1
                    y += 1
                return 1
            elif self.line < self.line2:
                x = self.line2-1
                m = self.line+1
                y = 1
                while x > self.line:
                    if self.row2 > self.row and self.arr[-m][self.row+(y*2)] != '.':
                        return 0
                    elif self.row2 < self.row and self.arr[-m][self.row-(y*2)] != '.':
                        return 0
                    x -= 1
                    m += 1
                    y += 1
                return 1
        if fig == 'q' or fig == 'Q':
            if self.line == self.line2:
                if self.row2 > self.row:
                    i = self.row+1
                    while i < self.row2:
                        if self.arr[-self.line][i] == ' ' or self.arr[-self.line][i] == '.':
                            i += 1
                        else:
                            return 0
                else:
                    i = self.row-1
                    while i > self.row2:
                        if self.arr[-self.line][i] == ' ' or self.arr[-self.line][i] == '.':
                            i -= 1
                        else:
                            return 0
                return 1
            elif self.row == self.row2:
                if self.line < self.line2:
                    i = self.line+1
                    while i < self.line2:
                        if self.arr[-i][self.row] == ' ' or self.arr[-i][self.row] == '.':
                            i += 1
                        else:
                            return 0
                else:
                    i = self.line-1
                    while i > self.line2:
                        if self.arr[-i][self.row] == ' ' or self.arr[-i][self.row] == '.':
                            i -= 1
                        else:
                            return 0
                return 1
            elif self.line > self.line2:
                x = self.line-1
                y = 1
                while x > self.line2:
                    if self.row2 > self.row and self.arr[-x][self.row+(y*2)] != '.':
                        return 0
                    elif self.row2 < self.row and self.arr[-x][self.row-(y*2)] != '.':
                        return 0
                    x -= 1
                    y += 1
                return 1
            elif self.line < self.line2:
                x = self.line2-1
                m = self.line+1
                y = 1
                while x > self.line:
                    if self.row2 > self.row and self.arr[-m][self.row+(y*2)] != '.':
                        return 0
                    elif self.row2 < self.row and self.arr[-m][self.row-(y*2)] != '.':
                        return 0
                    x -= 1
                    m += 1
                    y += 1
                return 1
        if fig == 'k' or fig == 'K':
            if self.check_rook() == 1:
                return 2
            else:
                if (self.line2 - self.line == 1 or self.line2 - self.line == -1 or self.line2 == self.line) and \
                        (self.row2 - self.row == 2 or self.row2 - self.row == -2 or self.row2 == self.row):
                    return 1
                else:
                    return 0

    def step(self):
        x = self.check_step(self.arr[-self.line][self.row])
        if self.check_position(self.line, self.row, self.line2, self.row2) == 1 and x == 1:
            figure = self.arr[-self.line][self.row]
            self.arr[-self.line] = self.arr[-self.line][:self.row] + '.' + self.arr[-self.line][self.row+1:]
            self.arr[-self.line2] = self.arr[-self.line2][:self.row2] + figure + self.arr[-self.line2][self.row2+1:]
            self.check_pawn()
        elif x == 2:
            print('Рокировка!')
        else:
            print('Такой ход совершить нельзя!')
            self.player -= 1
            self.get_step()
            self.step()

    def play(self):
        while self.counter != 1:
            self.counter = 0
            for i in self.arr:
                if 'k' in i or 'K' in i:
                    self.counter += 1
            self.show_board()
            self.get_step()
            self.step()

        print('Игра окончена!')
        if self.player % 2 == 0:
            print('Победа белых')
        else:
            print('Победа чёрных')


game = Game()
game.play()
