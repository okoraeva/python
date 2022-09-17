stones = {
    1: 100, 2: 15, 3: 20, 4: 90, 5: 7}
keys = []
# Создаем массив ключей
for key in stones.keys():
    keys.append(key)

weight = []

# Создаем массив значений-весов
for i in stones:
    weight.append(stones[i])

half_common = sum(weight) / 2
print(f'Среднее общее: {half_common}')

first = []
second = []
num = 0
num2 = 0
count = 0

# Распределяем "камни" по "кучам"
for i in weight:
    if (num + i) <= half_common:
        num += i
        first.append(keys[count])
        count += 1
    else:
        num2 += i
        second.append(keys[count])
        count += 1

print(f'В первой куче будут камни №{first}, их вес равен: {num}')
print(f'Во второй куче будут камни №{second}, их вес равен: {num2}')
