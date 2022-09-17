import random
num = []
while len(num) < 4:
    e = random.randint(0, 9)
    if not (e in num):
        num.append(e)
print(num)
user_input = input('Введите число: ')
user_num = [int(i) for i in str(user_input)]


def game(num, user_num):
    cows = 0
    bulls = 0
    i = 0
    while i < 4:
        if num[i] == user_num[i]:
            bulls += 1
        elif not(num[i] == user_num[i]) and num[i] in user_num:
            cows += 1
        i += 1
    print(f'Bulls: {bulls}, \nCows: {cows}')
    if not (bulls == 4):
        user_input = input('Введите число: ')
        user_num = [int(i) for i in str(user_input)]
        game(num, user_num)
    else:
        print('You won!')


game(num, user_num)
