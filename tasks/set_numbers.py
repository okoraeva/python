import random

def calc():
    global show_arr
    arr = []
    show_arr = []

    # Расставялем знаки между цифрами
    operations = ['+', '-', '']
    for i in range(1, 9):
        rand = random.randint(0, 2)
        arr.append(i)
        arr.append(operations[rand])
    arr.pop()

    arr = list(filter(None, arr))  # Убираем пустые сроки ''
    show_arr = arr  # Переменная для вывода массива

    # Объединяем цифры, между которыми были пустые строки ''
    num = ''
    i = 0
    while i < len(arr)-1:
        if isinstance(arr[i], int) and isinstance(arr[i+1], int):
            num += str(arr[i])
            num += str(arr[i+1])
            arr.pop(i)
            arr.pop(i)
            arr.insert(i, int(num))
            num = ''
        i += 1

    # Если число слишком большое, прекращаем функцию
    m = 1
    while m < len(arr):
        if not isinstance(arr[m], str):
            return [0]
        m += 2

    # Считаем количество минусов в массиве
    counter = 0
    for i in arr:
        if i == '-':
            counter += 1

    # Если перед числом стоит минус, делаем его отрицательным
    i = 0
    while i != counter:
        x = arr.index('-')
        arr[x+1] = -arr[x+1]
        arr.pop(x)
        i += 1
    print(arr)

    # Удаляем плюсы из массива
    for i in arr:
        if i == '+':
            arr.remove(i)

    return arr


calc()
count = 0
i = 0
while i < 150000:
    if sum(calc()) == 100:  # Считаем сумму массива, если равно 100, то выводим изначальный массив
        print(show_arr)
        count += 1
        calc()
    i += 1
print(count)
