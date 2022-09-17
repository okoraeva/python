arr = [" r n b q k b n r", " p p p p p p p p", " . . . . . . . .", " . . . . . . . .", " . . . . . . . .",
       " . . . . . . . .", " P P P P P P P P", " R N B Q K B N R"]
#arr = [" r n b q k b n r", " p p p p p p p p", " . . . . . . . .", " . . . . . P . .", " . . . . . . . .", " . . . . . . . .", " P P P P P . P P", " R N B Q K B N R"]
#arr = [" r n b q k b n .", " p p p p p p p P", " . . . . . . . .", " . . . . . . . .", " . . . . . . . .", " . . . . . . . .", " P P P P P P P P", " R N B Q K B N R"]
# " R N B Q K B N R"
# " R N B Q K . . R"
# " R . . . K B N R"
# " r n b q k b n r"
# " r . . . k b n r"
# " r n b q k . . r"
player = 1
line = 0
row = ''
line2 = 0
row2 = ''
counter = 0


def show_board(board):
    letter_row = "   A B C D E F G H"
    i = 0
    m = 8
    print(letter_row)
    print('   ---------------')
    while i < len(board):
        print(f'{m} {board[i]}  {m}')
        i += 1
        m -= 1
    print('   ---------------')
    print(letter_row)


def get_step():
    global player, line, line2, row, row2
    print(f'Ход номер {player}')
    if player % 2 == 0:
        print('Ходят чёрные')
    else:
        print('Ходят белые')
    user_input = list(input('Введите ход: '))
    if ' ' in user_input:
        user_input.remove(' ')
    if '-' in user_input:
        user_input.remove('-')
    if len(user_input) == 4:
        line = int(user_input[1])
        row = user_input[0]
        line2 = int(user_input[3])
        row2 = user_input[2]
    elif len(user_input) == 5 and user_input[0] in 'prnbqkPRNBQK':
        line = int(user_input[2])
        row = user_input[1]
        line2 = int(user_input[4])
        row2 = user_input[3]
    else:
        print('Неправильно введен ход!')
        get_step()
        step()
    row = check_index(row)
    row2 = check_index(row2)
    player += 1


def check_position(x, y, x2, y2):
    global arr
    # Проверка на правильночть ввода строки
    if x not in range(1, 9) or x2 not in range(1, 9):
        print('Неправильно выбрана строка')
        return 0
    # Проверка, что выбрано не пустое поле
    if arr[-x][y] == '.':
        print('Вы выбрали пустое поле, попробуйте ещё!')
        return 0
    # Проверка на правильность ввода ряда
    if arr[-x][y] in 'prnbqk' and arr[-x2][y2] not in 'prnbqk':
        return 1
    elif arr[-x][y] in 'PRNBQK' and arr[-x2][y2] not in 'PRNBQK':
        return 1
    else:
        print('Здесь стоит Ваша фигура!')
        return 0


def check_pawn():
    global arr, line, row, line2, row2
    if 'p' in arr[7]:
        figure = input('Выберите новую фигуру(r, n, b, q): ')
        while figure not in 'rnbqRNBQ':
            print('Вы ввели неправильную фигуру!')
            figure = input('Выберите новую фигуру(r, n, b, q): ')
        arr[-line2] = arr[-line2][:row2] + figure + arr[-line2][row2+1:]
    if 'P' in arr[0]:
        figure = input('Выберите новую фигуру(R, N, B, Q): ')
        while figure not in 'rnbqRNBQ':
            print('Вы ввели неправильную фигуру!')
            figure = input('Выберите новую фигуру(R, N, B, Q): ')
        arr[-line2] = arr[-line2][:row2] + figure + arr[-line2][row2+1:]
    if 'p' in arr[4] and line == 2 and line2 == 4 and (arr[4].index('p') - row2 == 2 or arr[4].index('p') - row2 == -2):
        arr[-line2] = arr[-line2][:row2] + '.' + arr[-line2][row2+1:]
        arr[-line2+1] = arr[-line2+1][:row2] + 'p' + arr[-line2+1][row2+1:]
        arr[4] = arr[4][:(arr[4].index('p'))] + '.' + arr[4][(arr[4].index('p'))+1:]
    if 'P' in arr[3] and line == 7 and line2 == 5 and (arr[3].index('P') - row2 == 2 or arr[3].index('P') - row2 == -2):
        arr[-line2] = arr[-line2][:row2] + '.' + arr[-line2][row2+1:]
        arr[-line2-1] = arr[-line2-1][:row2] + 'P' + arr[-line2-1][row2+1:]
        arr[3] = arr[3][:(arr[3].index('P'))] + '.' + arr[3][(arr[3].index('P'))+1:]


def check_rook():
    global arr, line, row, line2, row2
    if 'R . . . K' in arr[7] or 'K . . R' in arr[7]:
        if line2 == 1 and row2 == 5:
            arr[-line] = arr[-line][:9] + '.' + arr[-line][10:]
            arr[-line] = arr[-line][:row2] + 'K' + arr[-line][row2+1:]
            arr[-line] = arr[-line][:row2+2] + 'R' + arr[-line][row2+3:]
            arr[-line] = arr[-line][:1] + '.' + arr[-line][2:]
            return 1
        elif line2 == 1 and row2 == 13:
            arr[-line] = arr[-line][:9] + '.' + arr[-line][10:]
            arr[-line2] = arr[-line2][:row2] + 'K' + arr[-line2][row2+1:]
            arr[-line2] = arr[-line2][:11] + 'R' + arr[-line2][12:]
            arr[-line2] = arr[-line2][:15] + '.' + arr[-line2][16:]
            return 1
        else:
            return 0
    if 'r . . . k' in arr[0] or 'k . . r' in arr[0]:
        if line2 == 8 and row2 == 5:
            arr[-line] = arr[-line][:9] + '.' + arr[-line][10:]
            arr[-line] = arr[-line][:row2] + 'k' + arr[-line][row2+1:]
            arr[-line] = arr[-line][:row2+2] + 'r' + arr[-line][row2+3:]
            arr[-line] = arr[-line][:1] + '.' + arr[-line][2:]
            return 1
        elif line2 == 8 and row2 == 13:
            arr[-line] = arr[-line][:9] + '.' + arr[-line][10:]
            arr[-line2] = arr[-line2][:row2] + 'k' + arr[-line2][row2+1:]
            arr[-line2] = arr[-line2][:11] + 'r' + arr[-line2][12:]
            arr[-line2] = arr[-line2][:15] + '.' + arr[-line2][16:]
            return 1
        else:
            return 0


def check_index(x):
    global player
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
        player -= 1
        get_step()
    return row_position


def check_step(fig):
    global line2, line, row2, row, player, arr
    if fig == 'p' or fig == 'P':
        if row2 == row or ((row2 - row == 2 or row2 - row == -2) and (not arr[-line2][row2] == '.')):
            if fig == 'p':
                if (line == 7 and 4 < line2 < 7) or (line2 - line == -1):
                    return 1
                else:
                    return 0
            if fig == 'P':
                if (line == 2 and 2 < line2 < 5) or (line2 - line == 1):
                    return 1
                else:
                    return 0
        else:
            return 0
    if fig == 'r' or fig == 'R':
        if line == line2:
            if row2 > row:
                i = row+1
                while i < row2:
                    if arr[-line][i] == ' ' or arr[-line][i] == '.':
                        i += 1
                    else:
                        return 0
            else:
                i = row-1
                while i > row2:
                    if arr[-line][i] == ' ' or arr[-line][i] == '.':
                        i -= 1
                    else:
                        return 0
            return 1
        elif row == row2:
            if line < line2:
                i = line+1
                while i < line2:
                    if arr[-i][row] == ' ' or arr[-i][row] == '.':
                        i += 1
                    else:
                        return 0
            else:
                i = line-1
                while i > line2:
                    if arr[-i][row] == ' ' or arr[-i][row] == '.':
                        i -= 1
                    else:
                        return 0
            return 1
    if fig == 'n' or fig == 'N':
        if (line2 - line == 2 or line2 - line == -2) and (row2 - row == 2 or row2 - row == -2):
            return 1
        elif (line2 - line == 1 or line2 - line == -1) and (row2 - row == 4 or row2 - row == -4):
            return 1
        else:
            return 0
    if fig == 'b' or fig == 'B':
        if line > line2:
            x = line-1
            y = 1
            while x > line2:
                if row2 > row and arr[-x][row+(y*2)] != '.':
                    return 0
                elif row2 < row and arr[-x][row-(y*2)] != '.':
                    return 0
                x -= 1
                y += 1
            return 1
        elif line < line2:
            x = line2-1
            m = line+1
            y = 1
            while x > line:
                if row2 > row and arr[-m][row+(y*2)] != '.':
                    return 0
                elif row2 < row and arr[-m][row-(y*2)] != '.':
                    return 0
                x -= 1
                m += 1
                y += 1
            return 1
    if fig == 'q' or fig == 'Q':
        if line == line2:
            if row2 > row:
                i = row+1
                while i < row2:
                    if arr[-line][i] == ' ' or arr[-line][i] == '.':
                        i += 1
                    else:
                        return 0
            else:
                i = row-1
                while i > row2:
                    if arr[-line][i] == ' ' or arr[-line][i] == '.':
                        i -= 1
                    else:
                        return 0
            return 1
        elif row == row2:
            if line < line2:
                i = line+1
                while i < line2:
                    if arr[-i][row] == ' ' or arr[-i][row] == '.':
                        i += 1
                    else:
                        return 0
            else:
                i = line-1
                while i > line2:
                    if arr[-i][row] == ' ' or arr[-i][row] == '.':
                        i -= 1
                    else:
                        return 0
            return 1
        elif line > line2:
            x = line-1
            y = 1
            while x > line2:
                if row2 > row and arr[-x][row+(y*2)] != '.':
                    return 0
                elif row2 < row and arr[-x][row-(y*2)] != '.':
                    return 0
                x -= 1
                y += 1
            return 1
        elif line < line2:
            x = line2-1
            m = line+1
            y = 1
            while x > line:
                if row2 > row and arr[-m][row+(y*2)] != '.':
                    return 0
                elif row2 < row and arr[-m][row-(y*2)] != '.':
                    return 0
                x -= 1
                m += 1
                y += 1
            return 1
    if fig == 'k' or fig == 'K':
        if check_rook() == 1:
            return 2
        else:
            if (line2 - line == 1 or line2 - line == -1 or line2 == line) and (row2 - row == 2 or row2 - row == -2 or row2 == row):
                return 1
            else:
                return 0


def step():
    global player, arr, line, row, line2, row2
    x = check_step(arr[-line][row])
    if check_position(line, row, line2, row2) == 1 and x == 1:
        figure = arr[-line][row]
        arr[-line] = arr[-line][:row] + '.' + arr[-line][row+1:]
        arr[-line2] = arr[-line2][:row2] + figure + arr[-line2][row2+1:]
        check_pawn()
    elif x == 2:
        print('Рокировка!')
    else:
        print('Такой ход совершить нельзя!')
        player -= 1
        get_step()
        step()


while counter != 1:
    counter = 0
    for i in arr:
        if 'k' in i or 'K' in i:
            counter += 1
    show_board(arr)
    get_step()
    step()


print('Игра окончена!')
if player % 2 == 0:
    print('Победа белых')
else:
    print('Победа чёрных')
