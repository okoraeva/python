import csv
import methods


def load_table(file_name):
    arr = []
    with open(file_name, 'r') as f:
        file = csv.reader(f, delimiter=';')
        for i in file:
            arr.append(i)
        return arr


def save_table(file_name, *data):
    directory = open(file_name, 'w')
    writer = csv.writer(directory)
    writer.writerows(data)


def save_table_txt(file_name, data):
    directory = open(file_name, 'w')
    directory.write(str(methods.print_table(data)))
