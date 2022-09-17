class Game:

    def __init__(self):
        self.arr = ['', '123456789', '111213141', '516171819']
        self.num1 = 0
        self.num2 = 0
        self.user_line = 0
        self.user_line2 = 0
        self.user_row = 0
        self.user_row2 = 0
        self.next = 1

    def show_board(self):
        i = 0
        while i < len(self.arr):
            print(self.arr[i])
            i += 1

    def get_step(self):
        self.next = int(input('Введите 1 для совершения хода или 0 для переписания строк: '))
        if self.next == 1:  # Если введена 1, то происходит ход
            self.user_line = int(input('Введите строку: '))
            self.user_row = int(input('Введите столбец: '))
            if (self.user_row > 9 or self.user_row < 1) or (self.user_line > len(self.arr) or self.user_line < 0):
                print('Строка или столбец введен неправильно')
                self.get_step()
            else:
                self.num1 = self.arr[self.user_line][self.user_row - 1]
            print(self.num1)
            self.user_line2 = int(input('Введите строку: '))
            self.user_row2 = int(input('Введите столбец: '))
            if (self.user_row2 > 9 or self.user_row2 < 1) or (self.user_line2 > len(self.arr) or self.user_line2 < 0):
                print('Строка или столбец введен неправильно')
                self.get_step()
            else:
                self.num2 = self.arr[self.user_line2][self.user_row2 - 1]
            print(self.num2)
            self.step_main()
            self.show_board()
            self.get_step()
        elif self.next == 0:  # Если введен 0, то происходит перепись чисел
            self.rewrite_board()
        else:
            print('Такой ответ не подходит')

    def step(self):
        # Проверка, являются ли числа одинаковые или их сумма равна 10
        if (self.num1 == self.num2) or (int(self.num1) + int(self.num2) == 10):
            self.arr[self.user_line] = self.arr[self.user_line][:self.user_row - 1] + 'x' + \
                self.arr[self.user_line][self.user_row:]
            self.arr[self.user_line2] = self.arr[self.user_line2][:self.user_row2 - 1] + 'x' + \
                self.arr[self.user_line2][self.user_row2:]
        else:
            print('Такой ход совершить нельзя')

    def step_main(self):
        # Проверка на то, на каком расстоянии находятся цифры
        if self.user_line == self.user_line2:  # Если на одной строке
            if (self.user_row - self.user_row2 == 1) or (self.user_row - self.user_row2 == -1):
                self.step()
            else:
                new_arr = []
                lines = self.user_row - self.user_row2
                if lines > 1:
                    lines -= 1
                    rows = self.user_row - 1
                else:
                    lines += 1
                    rows = self.user_row + 1
                while not(lines == 0):
                    new_arr.append(self.arr[self.user_line][rows])
                    if lines > 0:
                        lines -= 1
                        rows -= 1
                    else:
                        rows += 1
                        lines += 1
                if new_arr == (['x'] * len(new_arr)):
                    self.step()
                else:
                    print('Такой ход совершить нельзя')
        elif (self.user_line - self.user_line2 == 1) or (self.user_line - self.user_line2 == -1):
            if self.user_row == self.user_row2:   # Если на одном ряду и соседних строках
                self.step()
            else:
                print('Такой ход совершить нельзя')
        else:
            if self.user_row == self.user_row2:   # Если на одном ряду, но не соседних строках
                new_arr = []
                rows = self.user_line - self.user_line2
                if rows > 1:
                    rows -= 1
                    lines = self.user_line - 1
                else:
                    rows += 1
                    lines = self.user_line + 1
                while not(rows == 0):
                    new_arr.append(self.arr[lines][self.user_row])
                    if rows > 0:
                        rows -= 1
                        lines -= 1
                    else:
                        lines += 1
                        rows += 1
                if new_arr == (['x'] * len(new_arr)):
                    self.step()
                else:
                    print('Такой ход совершить нельзя')
            else:
                print('Такой ход совершить нельзя')

    def rewrite_board(self):
        exam = ''
        for i in self.arr:
            j = i.replace(' ', '')
            j = j.replace('x', '')
            exam += j

        x = 0
        while x < len(exam):
            missed = 9 - len(self.arr[-1])
            if missed == 0:  # Если строка полная и состоят из 9 цифр, переписываем на другой ряд
                self.arr.append(exam[:9])
                exam = exam[9:]
            else:
                self.arr[-1] = self.arr[-1] + exam[:missed]  # Если строка неполная, то дополняем её
                exam = exam[missed:]
            x += 1

    def play(self):
        self.get_step()
        self.show_board()
        self.play()


game = Game()
game.show_board()
game.play()
