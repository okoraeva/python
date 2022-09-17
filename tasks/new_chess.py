'''Сложности:

    1. Придумать 3 новых вида фигур с оригинальными правилами перемещения и реализовать их классы. Создать модификацию шахмат с новыми фигурами с минимальным вмешательством в существующий код.

    2. На базе игры в шахматы реализовать игру в шашки. Разработать модификацию шахмат с минимальным вмешательством в существующий код.

    8. Реализовать поддержку для пешки сложных правил: «взятие на проходе» и замены на другух фигуру при достижении крайней горизонтали (в базовой версии их поддержка не обязательна, но возможность первого хода на одну или две горизонтали - обязательно). Подробнее о правилах см.: https://ru.wikipedia.org/wiki/Правила_шахмат . Информация о допустимых ходах должна храниться в объектно-ориентированном виде, алгоритм без модификации должен работать при добавлении новых типов фигур со сложным поведением (задание берется совместно с Заданием 1 и как минимум одна из новых фигур должна иметь сложное поведение, т.е. изменение правил хода и взятия фигуры в зависимости от дополнительных условий).

    Yenny - ходит как король и на +одну клетку больше в любую сторону, перепрыгивает через другие фигуры на пути (Пример: a2-c4)
    Enki - ходит как конь, только больше на +1 вертикально и +1 горизнтально (Пример: g3-e5, b2-e4)
    Monkey - ходит как ладья и слон вместе, при пересечении первой линии противники может стать любой фигурой на выбор как пешка
'''


class ChessFigure:

    def __init__(self, arr, line, row, line2, row2):
        self.arr = arr
        self.line = line
        self.row = row
        self.line2 = line2
        self.row2 = row2
        self.figure = arr[-line][row]


class King(ChessFigure):

    def check_move(self):
        if (self.line2 - self.line == 1 or self.line2 - self.line == -1 or self.line2 == self.line) and \
                (self.row2 - self.row == 2 or self.row2 - self.row == -2 or self.row2 == self.row):
            return 1
        else:
            return 0


class Queen(ChessFigure):

    def check_move(self):
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


class Bishop(ChessFigure):

    def check_move(self):
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


class Knight(ChessFigure):

    def check_move(self):
        if (self.line2 - self.line == 2 or self.line2 - self.line == -2) and (self.row2 - self.row == 2 or self.row2 - self.row == -2):
            return 1
        elif (self.line2 - self.line == 1 or self.line2 - self.line == -1) and (self.row2 - self.row == 4 or self.row2 - self.row == -4):
            return 1
        else:
            return 0


class Rook(ChessFigure):

    def check_move(self):
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


class Pawn(ChessFigure):

    def check_move(self):
        if self.row2 == self.row or ((self.row2 - self.row == 2 or self.row2 - self.row == -2) and (not self.arr[-self.line2][self.row2] == '.')):
            if self.figure == 'p':
                if (self.line == 7 and 4 < self.line2 < 7) or (self.line2 - self.line == -1):
                    return 1
                else:
                    return 0
            if self.figure == 'P':
                if (self.line == 2 and 2 < self.line2 < 5) or (self.line2 - self.line == 1):
                    return 1
                else:
                    return 0
        else:
            return 0


class Checkers(ChessFigure):

    def check_ladies(self):
        #  Проверяем вышла ли фигура в дамки
        if self.figure == 'o' and self.line2 == 1:
            self.figure = 'O'
            self.arr[-self.line2] = self.arr[-self.line2][:self.row2] + self.figure + self.arr[-self.line2][self.row2+1:]
        if self.figure == '0' and self.line2 == 8:
            self.figure = '8'
            self.arr[-self.line2] = self.arr[-self.line2][:self.row2] + self.figure + self.arr[-self.line2][self.row2+1:]

    def check_move(self):
        if self.figure in 'o0':
            if self.line - self.line2 == 1 or self.line - self.line2 == -1:
                if (self.row - self.row2 == -2 or self.row - self.row2 == 2) and self.arr[-self.line2][self.row2] == '.':
                    return 1
            elif self.line - self.line2 == -2:
                if self.row - self.row2 == -4 and self.arr[-self.line2+1][self.row2-2] != '.' and self.arr[-self.line2][self.row2] == '.':
                    self.arr[-self.line2+1] = self.arr[-self.line2+1][:self.row2-2] + '.' + self.arr[-self.line2+1][self.row2-1:]
                    return 1
                elif self.row - self.row2 == 4 and self.arr[-self.line2+1][self.row2+2] != '.' and self.arr[-self.line2][self.row2] == '.':
                    self.arr[-self.line2+1] = self.arr[-self.line2+1][:self.row2+2] + '.' + self.arr[-self.line2+1][self.row2+3:]
                    return 1
            elif self.line - self.line2 == 2:
                if self.row - self.row2 == -4 and self.arr[-self.line2-1][self.row2-2] != '.' and self.arr[-self.line2][self.row2] == '.':
                    self.arr[-self.line2-1] = self.arr[-self.line2+1][:self.row2-2] + '.' + self.arr[-self.line2+1][self.row2-1:]
                    return 1
                elif self.row - self.row2 == 4 and self.arr[-self.line2-1][self.row2+2] != '.' and self.arr[-self.line2][self.row2] == '.':
                    self.arr[-self.line2-1] = self.arr[-self.line2+1][:self.row2+2] + '.' + self.arr[-self.line2+1][self.row2+3:]
                    return 1
            else:
                return 0
        else:
            if self.line > self.line2:
                x = self.line-1
                y = 1
                while x > self.line2:
                    if self.figure == 'O':
                        if self.row2 > self.row and self.arr[-x][self.row+(y*2)] == 'o':
                            return 0
                        else:
                            self.arr[-x] = self.arr[-x][:self.row+(y*2)] + '.' + self.arr[-x][self.row+(y*2)+1:]
                        if self.row2 < self.row and self.arr[-x][self.row-(y*2)] == 'o':
                            return 0
                        else:
                            self.arr[-x] = self.arr[-x][:self.row+(y*2)] + '.' + self.arr[-x][self.row+(y*2)+1:]
                    elif self.figure == '8':
                        if self.row2 > self.row and self.arr[-x][self.row+(y*2)] == '0':
                            return 0
                        elif self.row2 < self.row and self.arr[-x][self.row-(y*2)] == '0':
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


class Yenny(ChessFigure):

    def check_move(self):
        if (self.line2 - self.line == 1 or self.line2 - self.line == -1 or self.line2 == self.line) and \
                (self.row2 - self.row == 2 or self.row2 - self.row == -2 or self.row2 == self.row):
            return 1
        elif (self.line2 - self.line == 2 or self.line2 - self.line == -2 or self.line2 == self.line) and \
                (self.row2 - self.row == 4 or self.row2 - self.row == -4 or self.row2 == self.row):
            return 1
        else:
            return 0


class Enki(ChessFigure):

    def check_move(self):
        if (self.line2 - self.line == 3 or self.line2 - self.line == -3) and (self.row2 - self.row == 4 or self.row2 - self.row == -4):
            return 1
        elif (self.line2 - self.line == 2 or self.line2 - self.line == -2) and (self.row2 - self.row == 6 or self.row2 - self.row == -6):
            return 1
        else:
            return 0


class Monkey(ChessFigure):

    def check_move(self):
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
        elif self.line == self.line2:
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


class Step:

    def __init__(self, arr, player):
        self.arr = arr
        self.player = player
        self.line = 0
        self.row = ''
        self.line2 = 0
        self.row2 = ''
        self.counter = 0

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
        self.row = self.check_index(self.row)
        self.row2 = self.check_index(self.row2)
        self.player += 1
        return self.player

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

    def check_monkey(self):
        if 'm' in self.arr[7]:
            figure = input('Выберите новую фигуру(r, n, b, q, y, e, m): ')
            while figure not in 'rnbqyemRNBQYEM':
                print('Вы ввели неправильную фигуру!')
                figure = input('Выберите новую фигуру(r, n, b, q, y, e, m): ')
            self.arr[-self.line2] = self.arr[-self.line2][:self.row2] + figure + self.arr[-self.line2][self.row2+1:]
        if 'M' in self.arr[0]:
            figure = input('Выберите новую фигуру(R, N, B, Q, Y, E, M): ')
            while figure not in 'rnbqyemRNBQYEM':
                print('Вы ввели неправильную фигуру!')
                figure = input('Выберите новую фигуру(R, N, B, Q, Y, E, M): ')
            self.arr[-self.line2] = self.arr[-self.line2][:self.row2] + figure + self.arr[-self.line2][self.row2+1:]

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
        if self.arr[-x][y] in 'prnbqkyem' and self.arr[-x2][y2] not in 'prnbqkyem':
            return 1
        elif self.arr[-x][y] in 'PRNBQKYEM' and self.arr[-x2][y2] not in 'PRNBQKYEM':
            return 1
        elif self.arr[-x][y] in 'oO' and self.arr[-x2][y2] not in 'oO':
            return 1
        elif self.arr[-x][y] in '08' and self.arr[-x2][y2] not in '08':
            return 1
        else:
            print('Здесь стоит Ваша фигура!')
            return 0

    def make_step(self):
        figure = self.arr[-self.line][self.row]
        if figure in 'kK':
            king = King(self.arr, self.line, self.row, self.line2, self.row2)
            x = king.check_move()
        elif figure in 'qQ':
            queen = Queen(self.arr, self.line, self.row, self.line2, self.row2)
            x = queen.check_move()
        elif figure in 'bB':
            bishop = Bishop(self.arr, self.line, self.row, self.line2, self.row2)
            x = bishop.check_move()
        elif figure in 'nN':
            knight = Knight(self.arr, self.line, self.row, self.line2, self.row2)
            x = knight.check_move()
        elif figure in 'rR':
            rook = Rook(self.arr, self.line, self.row, self.line2, self.row2)
            x = rook.check_move()
        elif figure in 'pP':
            pawn = Pawn(self.arr, self.line, self.row, self.line2, self.row2)
            x = pawn.check_move()
        elif figure in 'yY':
            yenny = Yenny(self.arr, self.line, self.row, self.line2, self.row2)
            x = yenny.check_move()
        elif figure in 'eE':
            enki = Enki(self.arr, self.line, self.row, self.line2, self.row2)
            x = enki.check_move()
        elif figure in 'mM':
            monkey = Monkey(self.arr, self.line, self.row, self.line2, self.row2)
            x = monkey.check_move()
        if figure in 'o0O8':
            checker = Checkers(self.arr, self.line, self.row, self.line2, self.row2)
            x = checker.check_move()
        else:
            checker = 0
        if self.check_position(self.line, self.row, self.line2, self.row2) == 1 and x == 1:
            self.arr[-self.line] = self.arr[-self.line][:self.row] + '.' + self.arr[-self.line][self.row+1:]
            self.arr[-self.line2] = self.arr[-self.line2][:self.row2] + figure + self.arr[-self.line2][self.row2+1:]
            self.check_pawn()
            self.check_monkey()
            if checker != 0:
                checker.check_ladies()
        else:
            print('Такой ход совершить нельзя!')
            self.player -= 1
            self.get_step()
            self.make_step()
        return self.arr


class Board:

    def __init__(self, arr):
        self.arr = arr

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


class Play:

    def __init__(self):
        self.arr = [" r n b q k b n r", " p p p p p p p p", " . . . . . . . .", " . . . . . . . .", " . . . . . . . .",\
                    " . . . . . . . .", " P P P P P P P P", " R N B Q K B N R"]
        self.arr1 = [" . o . o . o . o", " o . o . o . o .", " . o . o . o . o",  " . . . . . . . .", \
                     " . . . . . . . .", " 0 . 0 . 0 . 0 .", " . 0 . 0 . 0 . 0", " 0 . 0 . 0 . 0 ."]
        self.arr2 = [" r n b q k b n r", " y e m p p m e y", " . . . . . . . .", " . . . . . . . .", " . . . . . . . .",\
                     " . . . . . . . .", " Y E M P P M E Y", " R N B Q K B N R"]
        self.counter = 0
        self.checker_counter1 = 0
        self.checker_counter2 = 0
        self.player = 1

    def run_chess(self):
        while self.counter != 1:
            self.counter = 0
            for i in self.arr:
                if 'k' in i or 'K' in i:
                    self.counter += 1
            board = Board(self.arr)
            step = Step(self.arr, self.player)
            board.show_board()
            self.player = step.get_step()
            self.arr = step.make_step()

        print('Игра окончена!')
        if self.player % 2 == 0:
            print('Победа белых')
        else:
            print('Победа чёрных')

    def run_chess_new(self):
        while self.counter != 1:
            self.counter = 0
            for i in self.arr2:
                if 'k' in i or 'K' in i:
                    self.counter += 1
            board = Board(self.arr2)
            step = Step(self.arr2, self.player)
            board.show_board()
            self.player = step.get_step()
            self.arr2 = step.make_step()

        print('Игра окончена!')
        if self.player % 2 == 0:
            print('Победа белых')
        else:
            print('Победа чёрных')

    def run_checkers(self):
        for j in self.arr1:
            self.checker_counter1 += j.count('o')
            self.checker_counter1 += j.count('O')
            self.checker_counter2 += j.count('0')
            self.checker_counter2 += j.count('8')
        while self.checker_counter1 != 0 and self.checker_counter2 != 0:
            board = Board(self.arr1)
            step = Step(self.arr1, self.player)
            board.show_board()
            self.player = step.get_step()
            self.arr1 = step.make_step()
            self.checker_counter1 = 0
            self.checker_counter2 = 0
            for j in self.arr1:
                self.checker_counter1 += j.count('o')
                self.checker_counter1 += j.count('O')
                self.checker_counter2 += j.count('0')
                self.checker_counter2 += j.count('8')

        print('Игра окончена!')
        if self.player % 2 == 0:
            print('Победа белых')
        else:
            print('Победа чёрных')


play = Play()

# Запускает шахматы
# play.run_chess()

# Запускает шахматы с новыми фигурами
# play.run_chess_new()

# Запускает шашки
play.run_checkers()

