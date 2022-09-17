import csv
import os


def load_table(file_name):
    arr = []
    with open(file_name, 'r') as f:
        file = csv.reader(f)
        for i in file:
            arr.append(i)
        return arr


arr = load_table('/home/olya/Рабочий стол/python/py_task/ex.txt')

print("Все папки и файлы:", os.listdir())
list_files = os.listdir()

i = 0
while i < len(arr):
    x = ''.join(arr[i])
    if x in list_files:
        os.remove(x)
    i += 1

print("Все папки и файлы:", os.listdir())