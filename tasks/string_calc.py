import math
PI = 3.14

numbers = {"ноль": 0, "нулю": 0, "один": 1, "одна": 1, "одному": 1, "одного": 1, "два": 2, "две": 2, "двух": 2,
           "двум": 2, "три": 3, "трех": 3, "трёх": 3, "трем": 3, "трём": 3, "четыре": 4, "четырех": 4, "четырем": 4,
           "пять": 5, "пяти": 5, "шесть": 6, "шести": 6, "семь": 7, "семи": 7, "восемь": 8, "восьми": 8, "девять": 9,
           "девяти": 9, "десять": 10, "десяти": 10, "одиннадцать": 11, "одиннадцати": 11, "двенадцать": 12,
           "двенадцати": 12, "тринадцать": 13, "тринадцати": 13, "четырнадцать": 14, "четырнадцати": 14,
           "пятнадцать": 15, "пятнадцати": 15, "шестнадцать": 16, "шестнадцати": 16, "семнадцать": 17, "семнадцати": 17,
           "восемнадцать": 18, "восемнадцати": 18, "девятнадцать": 19, "девятнадцати": 19, "двадцать": 20,
           "двадцати": 20, "тридцать": 30, "тридцати": 30, "сорок": 40, "сорока": 40, "пятьдесят": 50, "пятидесяти": 50,
           "шестьдесят": 60, "шестидесяти": 60, "семьдесят": 70, "семидесяти": 70, "восемьдесят": 80,
           "восьмидесяти": 80, "девяносто": 90, "девяноста": 90, "сто": 100, "ста": 100, "двести": 200, "двухста": 200,
           "триста": 300, "трехста": 300, "четыреста": 400, "четырехсот": 400, "пятьсот": 500, "пятиста": 500,
           "шестьсот": 600, "шестиста": 600, "семьсот": 700, "семиста": 700, "восемьсот": 800, "восьмиста": 800,
           "девятьсот": 900, "девятиста": 900, "плюс": '+', "минус": '-', "умножить": '*', "делить": '/',
           "разделить": '/', "и": 'и', "целых": 'целых', "десятых": 'десятых', "десятая": 'десятая', "сотых": 'сотых',
           "сотая": 'сотая', "тысячных": 'тысячных', "тысячная": 'тысячная', "десятитысячных": 'десятитысячных',
           "десятитысячная": 'десятитысячная', "стотысячных": 'стотысячных', "стотысячная": 'стотысячная',
           "миллионных": 'миллионных', "миллионная": 'миллионная', "тысяч": 'тысяч', "размещение": 'размещение',
           "размещений": 'размещение', "перестановка": 'перестановка', "перестановок": 'перестановка',
           "сочетание": 'сочетание', "сочетаний": 'сочетание', "по": 'по', "степени": '**', "синус": 'синус',
           "пи": PI, "косинус": 'косинус', "тангенс": 'тангенс'}

values = {0: "ноль", 1: "один", "одна": 'одна', 2: "два", "две": 'две', 3: "три", 4: "четыре", 5: "пять", 6: "шесть",
          7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать",
          14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать",
          19: "девятнадцать", 20: "двадцать", 30: "тридцать", 40: "сорок", 50: "пятьдесят", 60: "шестьдесят",
          70: "семьдесят", 80: "восемьдесят", 90: "девяносто", 100: "сто", 200: "двести", 300: "триста",
          400: "четыреста", 500: "пятьсот", 600: "шестьсот", 700: "семьсот", 800: "восемьсот", 900: "девятьсот",
          1000: "тысяча"}


keys = numbers.keys()
operations = ['+', '-', '*', '/', '**']
line_operations = ["размещение", "размещений", "перестановка", "перестановок", "сочетание", "сочетаний"]
word_check = ["и", "целых", "десятых", "десятая", "сотых", "сотая", "тысячных", "тысячная", "десятитысячных",
              "десятитысячная", "стотысячных", "стотысячная", "миллионных", "миллионная", "тысяч", "размещение",
              "перестановка", "сочетание", "по", "степени", "синус", "пи", "косинус", "тангенс", "+", "-", "/", "*",
              "**"]


def get_precision(f):
    str_f = str(f)
    if '.' not in str_f:
        return 0
        # Получение строки после точки и возвращение ее длины
    return len(str_f[str_f.index('.') + 1:])


# Метод для разделения двухзначного числа по разрядам, используется при выводе ответа
def div(num):
    array = [num // 100 * 100, num // 10 % 10 * 10, num % 10]
    i = 0
    while i < len(array):
        if array[i] == 0:
            array.remove(array[i])
            i -= 1
        i += 1
    return array


def calc(user_num):
    answer = 0

    # Удаляем ненужные предлоги из массива
    if 'на' in user_num:
        user_num.remove('на')
    if 'из' in user_num:
        user_num.remove('из')
    if 'в' in user_num:
        user_num.remove('в')
    if 'от' in user_num:
        user_num.remove('от')

    # Проверка написания слов и порядка написания операций: "размещение", "перестановка", "сочетание"
    for i in user_num:
        if i not in keys:
            print(f'Неправильно введено значение: {i}')
            print('Попробуйте ещё раз')
            new_num = str(input('Строка для ввода: ')).split(' ')
            return calc(new_num)
        if i in line_operations and not user_num.index(i) == 0:
            print(f'Операция "{i}" указана не в том месте!')
            print('Попробуйте ещё раз')
            new_num = str(input('Строка для ввода: ')).split(' ')
            return calc(new_num)

    # Переводим цифры из строк в числа
    for i in range(0, len(user_num)):
        user_num[i] = numbers.get(user_num[i])

    # Проверка правильного порядка написания операций
    i = 0
    while i < len(user_num)-1:
        if not user_num[i+1] in word_check and not user_num[i] in word_check:
            if user_num[i] < user_num[i+1]:
                print('Неправильный порядок цифр')
                print('Попробуйте ещё раз')
                new_num = str(input('Строка для ввода: ')).split(' ')
                return calc(new_num)
        i += 1

    # Присваиваем переменной action операцию
    if '+' in user_num:
        action = 'плюс'
    elif '-' in user_num:
        action = 'минус'
    elif '*' in user_num:
        action = 'умножить'
    elif '/' in user_num:
        action = 'делить'
    elif 'размещение' in user_num:
        action = 'размещение'
        replace = user_num.index('по')
        user_num.remove('по')
        user_num.insert(replace, action)  # Меняем местами 'размещение' и 'по' для удобства вычислений
        user_num.pop(0)
    elif 'перестановка' in user_num:
        action = 'перестановка'
    elif 'сочетание' in user_num:
        action = 'сочетание'
        replace = user_num.index('по')
        user_num.remove('по')
        user_num.insert(replace, action)  # Меняем местами 'сочетание' и 'по' для удобства вычислений
        user_num.pop(0)
    elif '**' in user_num:
        action = 'степени'
    else:
        print('Вы не ввели операцию!')
        print('Попробуйте ещё раз')
        new_num = str(input('Строка для ввода: ')).split(' ')
        return calc(new_num)

    # Проверка порядка операций
    if user_num[0] in operations:
        print('Неправильный порядок операций, операция стоит на первом месте!')
        print('Попробуйте ещё раз')
        new_num = str(input('Строка для ввода: ')).split(' ')
        return calc(new_num)
    elif user_num[-1] in operations:
        print('Неправильный порядок операций, операция стоит на последнем месте!')
        print('Попробуйте ещё раз')
        new_num = str(input('Строка для ввода: ')).split(' ')
        return calc(new_num)

    # Разделяем масссив на два числа
    if action == 'перестановка':  # Если выполняется операция "перестановка", то второе число не нужно
        user_num.remove('перестановка')
        first_num = user_num
        sec_num = []
    else:
        operand = user_num.index(numbers.get(action))  # индекс вхождения операции в массив для получения срезов
        first_num = user_num[:operand]
        sec_num = user_num[operand+1:]

    # Если введено число с десятичной дробью, находим его и соединяем разряды
    def check_frac(arr):
        acc = 0

        # Если у дроби есть целая часть, то отсоединяем её и присваемаем переменной acc
        if 'целых' in arr:
            x = arr.index('целых')
            acc = arr[:x]
            arr.remove('целых')
        elif 'и' in arr:
            x = arr.index('и')
            acc = arr[:x]
            arr.remove('и')
        for i in acc:
            arr.remove(i)
        acc = sum(acc)

        # Если при написании используется слово тысяч, то также отделяем его и присваиваем переменной add_th
        if 'тысяч' in arr:
            x = arr.index('тысяч')
            add_th = arr[:x]
            arr.remove('тысяч')
            for i in add_th:
                arr.remove(i)
            add_th = sum(add_th) * 1000
        else:
            add_th = 0

        if 'десятых' in arr or 'десятая' in arr:
            arr.pop()
            arr = (sum(arr) + add_th) / 10
            arr += acc
            return arr
        if 'сотых' in arr or 'сотая' in arr:
            arr.pop()
            arr = (sum(arr) + add_th) / 100
            arr += acc
            return arr
        if 'тысячных' in arr or 'тысячная' in arr:
            arr.pop()
            arr = (sum(arr) + add_th) / 1000
            arr += acc
            return arr
        if 'десятитысячных' in arr or 'десятитысячная' in arr:
            arr.pop()
            arr = (sum(arr) + add_th) / 10000
            arr += acc
            return arr
        if 'стотысячных' in arr or 'стотысячная' in arr:
            arr.pop()
            arr = (sum(arr) + add_th) / 100000
            arr += acc
            return arr
        if 'миллионных' in arr or 'миллионная' in arr:
            arr.pop()
            arr = (sum(arr) + add_th) / 1000000
            arr += acc
            return arr

    # Слово "целых" и "и" указывает, что есть десятичная дробь, используем функцию check_frac, чтобы найти его и
    # обработать, делаем проверку для первого числа
    if 'целых' in first_num or 'и' in first_num:
        first_num = check_frac(first_num)
    else:
        if 'синус' in first_num:  # Для правильной обработки операций синус, косинус, тангенс
            first_num.remove('синус')
            first_num = sum(first_num)   # Соединяем разряды первого числа
            # ТК math.sin и аналогичные операции принимают значение в радианах, то градусы нужно перевести в радианы
            # при помощи функции math.radians, но число пи переводить не нужно, поэтому оно вынесено отдельно
            if first_num == PI:
                first_num = round(math.sin(first_num), 3)
            else:
                first_num = round(math.sin(math.radians(first_num)), 3)
        elif 'косинус' in first_num:
            first_num.remove('косинус')
            first_num = sum(first_num)   # Соединяем разряды первого числа
            if first_num == PI:
                first_num = round(math.cos(first_num), 3)
            else:
                first_num = round(math.cos(math.radians(first_num)), 3)
        elif 'тангенс' in first_num:
            first_num.remove('тангенс')
            first_num = sum(first_num)   # Соединяем разряды первого числа
            if first_num == PI:
                first_num = round(math.tan(first_num), 3)
            else:
                if first_num == 90 or first_num == 270:
                    print('Тангенса такого градуса не существует!')
                    print('Попробуйте ещё раз')
                    new_num = str(input('Строка для ввода: ')).split(' ')
                    return calc(new_num)
                else:
                    first_num = round(math.tan(math.radians(first_num)), 3)
        else:
            first_num = sum(first_num)   # Соединяем разряды первого числа

    # Такая же проверка для второго числа
    if 'целых' in sec_num or 'и' in sec_num:
        sec_num = check_frac(sec_num)
    else:
        if 'синус' in sec_num:
            sec_num.remove('синус')
            sec_num = sum(sec_num)   # Соединяем разряды первого числа
            if sec_num == PI:
                sec_num = round(math.sin(sec_num), 3)
            else:
                sec_num = round(math.sin(math.radians(sec_num)), 3)
        elif 'косинус' in sec_num:
            sec_num.remove('косинус')
            sec_num = sum(sec_num)   # Соединяем разряды первого числа
            if sec_num == PI:
                sec_num = round(math.cos(sec_num), 3)
            else:
                first_num = round(math.cos(math.radians(sec_num)), 3)
        elif 'тангенс' in sec_num:
            sec_num.remove('тангенс')
            sec_num = sum(sec_num)   # Соединяем разряды первого числа
            if sec_num == PI:
                sec_num = round(math.tan(sec_num), 3)
            else:
                if sec_num == 90 or sec_num == 270:
                    print('Тангенса такого градуса не существует!')
                    print('Попробуйте ещё раз')
                    new_num = str(input('Строка для ввода: ')).split(' ')
                    return calc(new_num)
                else:
                    sec_num = round(math.tan(math.radians(sec_num)), 3)
        else:
            sec_num = sum(sec_num)  # Соединяем разряды второго числа

    # Проводим операцию
    if action == 'плюс':
        answer = first_num + sec_num
    elif action == 'минус':
        answer = first_num - sec_num
    elif action == 'умножить':
        answer = first_num * sec_num
    elif action == 'делить':
        if sec_num == 0:
            print('Операцию совершить нельзя, деление на ноль запрещено!')
            print('Попробуйте ещё раз')
            new_num = str(input('Строка для ввода: ')).split(' ')
            return calc(new_num)
        answer = first_num / sec_num
    elif action == 'размещение':
        answer = math.factorial(first_num) / math.factorial(first_num - sec_num)
    elif action == 'перестановка':
        answer = math.factorial(first_num)
    elif action == 'сочетание':
        answer = math.factorial(first_num) / math.factorial(first_num - sec_num) * math.factorial(sec_num)
    elif action == 'степени':
        answer = first_num ** sec_num

    answer = round(answer, 9)

    # Выводим ответ в строковом виде
    if answer % 1 == 0:  # Проверка на целое число
        if answer > 19:
            pic = div(answer)  # div разделяет числа по разрядам
        else:
            pic = [answer]
        res = ""
        for i in pic:
            res += f'{values.get(i)} '
        return f'Ответ: {res}'
    else:
        reloc_th = 0
        tenth_arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        whole = answer // 1  # Получаем два значения: дробную часть и целую часть
        frac = round(answer % 1, 6)
        count = get_precision(frac)  # Считает количество знаков после запятой для вывода
        if frac <= 0.000099:  # Почему-то неправильно выводит значения чисел меньше 0.000099, count = 5, а должен = 6
            count = 6
        first = div(whole)
        if len(first) == 0:  # Для вывода правильной целой части, если она равна 0
            first.append(0)
        if count == 1:  # Если количество знаков после запятой равно 1
            sec = div(frac*10)  # div разделяет числа по разрядам
            if round(sec[-1], 2) == 2:  # Для правильного вывода н-р "две десятых" вместо "два десятых"
                sec[-1] = 'две '
            elif round(sec[-1], 2) == 1:  # Для правильного вывода "одна десятая" вместо "один десятых"
                sec[-1] = 'одна '
            res = ""
            for i in first:  # Находим сторковые аналоги чисел в values для целой части
                res += f'{values.get(i)} '
            res += 'целых '
            for i in sec:  # Находим сторковые аналоги чисел в values для дробной части
                if isinstance(i, str):
                    res += i
                    if i == 'одна ':
                        res += 'десятая'
                else:
                    res += f'{values.get(round(i, 0))} '
            if 'десятая' not in res:
                res += 'десятых'
            return f'Ответ: {res}'
        elif count == 2:
            sec = div(frac*100)  # div разделяет числа по разрядам
            if round(sec[-1], 2) == 2:
                sec[-1] = 'две '
            elif round(sec[-1], 2) == 1:
                sec[-1] = 'одна '
            res = ""
            for i in first:
                res += f'{values.get(i)} '
            res += 'целых '
            for i in sec:
                if isinstance(i, str):
                    res += i
                    if i == 'одна ':
                        res += 'сотая'
                else:
                    res += f'{values.get(round(i, 0))} '
            if 'сотая' not in res:
                res += 'сотых'
            return f'Ответ: {res}'
        elif count == 3:
            sec = div(frac*1000)  # div разделяет числа по разрядам
            if round(sec[-1], 2) == 2:
                sec[-1] = 'две '
            elif round(sec[-1], 2) == 1:
                sec[-1] = 'одна '
            res = ""
            for i in first:
                res += f'{values.get(i)} '
            res += 'целых '
            for i in sec:
                if isinstance(i, str):
                    res += i
                    if i == 'одна ':
                        res += 'тысячная'
                else:
                    res += f'{values.get(round(i, 0))} '
            if 'тысячная' not in res:
                res += 'тысячных'
            return f'Ответ: {res}'
        elif count == 4:
            sec = div(frac*10000)  # div разделяет числа по разрядам
            if sec[0] > 1000:  # Если значение первого числа больше тысячи, делим его на 1000 для правильного вывода
                sec[0] = sec[0] / 1000
                add_thous = 1
            else:
                add_thous = 0
            if round(sec[-1], 2) == 2:
                sec[-1] = 'две '
            elif round(sec[-1], 2) == 1:
                sec[-1] = 'одна '
            res = ""
            for i in first:
                res += f'{values.get(i)} '
            res += 'целых '
            for i in sec:
                if isinstance(i, str):
                    res += i
                    if i == 'одна ':
                        res += 'десятитысячная'
                else:
                    if add_thous == 1:
                        res += f'{values.get(round(i, 0))} '
                        res += 'тысяч '
                        add_thous = 0
                    else:
                        res += f'{values.get(round(i, 0))} '
            if 'десятитысячная' not in res:
                res += 'десятитысячных'
            return f'Ответ: {res}'
        elif count == 5:
            sec = div(frac*100000)  # div разделяет числа по разрядам
            if sec[0] > 1000:
                sec[0] = sec[0] / 1000
                if sec[0] > 19 and not sec[0] in tenth_arr:
                    reloc_th = 1
                    sec[0] = div(sec[0])
                else:
                    reloc_th = 0
                add_thous = 1
            else:
                add_thous = 0
            print(sec)
            if round(sec[-1], 2) == 2:
                sec[-1] = 'две '
            elif round(sec[-1], 2) == 1:
                sec[-1] = 'одна '
            res = ""
            for i in first:
                res += f'{values.get(i)} '
            res += 'целых '
            for i in sec:
                if isinstance(i, str):
                    res += i
                    if i == 'одна ':
                        res += 'стотысячная'
                else:
                    if add_thous == 1:
                        if reloc_th == 1:
                            for j in i:
                                res += f'{values.get(round(j, 0))} '
                        else:
                            res += f'{values.get(round(i, 0))} '
                        res += 'тысяч '
                        add_thous = 0
                    else:
                        res += f'{values.get(round(i, 0))} '
            if 'стотысячная' not in res:
                res += 'стотысячных'
            return f'Ответ: {res}'
        elif count == 6:
            sec = div(frac*1000000)  # div разделяет числа по разрядам
            if sec[0] > 1000:
                sec[0] = sec[0] / 1000
                if sec[0] > 19 and not sec[0] in tenth_arr:
                    reloc_th = 1
                    sec[0] = div(sec[0])
                else:
                    reloc_th = 0
                add_thous = 1
            else:
                add_thous = 0
            print(sec)
            res = ""
            if round(sec[-1], 2) == 2:
                sec[-1] = 'две '
            elif round(sec[-1], 2) == 1:
                sec[-1] = 'одна '
            print(sec)
            for i in first:
                res += f'{values.get(i)} '
            res += 'целых '
            for i in sec:
                if isinstance(i, str):
                    res += i
                    if i == 'одна ':
                        res += 'миллионная'
                else:
                    if add_thous == 1:
                        if reloc_th == 1:
                            for j in i:
                                res += f'{values.get(round(j, 0))} '
                        else:
                            res += f'{values.get(round(i, 0))} '
                        res += 'тысяч '
                        add_thous = 0
                    else:
                        res += f'{values.get(round(i, 0))} '
            if 'миллионная' not in res:
                res += 'миллионных'
            return f'Ответ: {res}'


user_input = str(input('Строка для ввода: ')).split(' ')
print(calc(user_input))
