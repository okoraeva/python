import csv
from statistics import mean

arr = []
with open('/home/olya/Рабочий стол/python/tasks/value.csv', 'r') as f:
    file = csv.reader(f, delimiter=';')
    for i in file:
        arr.append(i)

eur = []
lse = []
usa = []

for i in arr:
    if i[1] == 'EUR':
        eur.append(int(i[2].replace(" ", "")))
    elif i[1] == 'LSE':
        lse.append(int(i[2].replace(" ", "")))
    elif i[1] == 'USA':
        usa.append(int(i[2].replace(" ", "")))

print(f'Среднее значение объема по EUR: {round(mean(eur), 2)}')
print(f'Среднее значение объема по LSE: {round(mean(lse), 2)}')
print(f'Среднее значение объема по USA: {round(mean(usa), 2)}')
print(f'Максимальное значение объема по EUR: {max(eur)}')
print(f'Максимальное значение объема по LSE: {max(lse)}')
print(f'Максимальное значение объема по USA: {max(usa)}')
print(f'Минимальное значение объема по EUR: {min(eur)}')
print(f'Минимальное значение объема по LSE: {min(lse)}')
print(f'Минимальное значение объема по USA: {min(usa)}')
