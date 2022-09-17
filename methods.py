import csv_module
from prettytable import PrettyTable


def get_rows_by_number(file_name, start, stop, copy_table=False):
    output_directory = '/home/olya/Рабочий стол/python/get_rows_by_number.csv'
    try:
        assert start <= stop, 'Неправильный интервал start-stop'
    except AssertionError as e:
        print(e)
    try:
        file = csv_module.load_table(file_name)
        sliced_file = file[start:stop+1]
        if copy_table:
            csv_module.save_table(output_directory, *sliced_file)
        for row in sliced_file:
            print(row)
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')


def get_rows_by_index(file_name, copy_table=False, **val):
    output_directory = '/home/olya/Рабочий стол/python/get_rows_by_index.csv'
    try:
        arr = []
        file = csv_module.load_table(file_name)
        keys = val.values()
        for i in keys:
            for j in file:
                if i in j:
                    arr.append(j)
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')
    if copy_table:
        csv_module.save_table(output_directory, *arr)
    for el in arr:
        print(el)


def get_column_types(file_name, by_number=True):
    # output_directory = '/home/olya/Рабочий стол/python/get_column_types.csv'
    my_list = {}
    try:
        file = csv_module.load_table(file_name)
        headers = file[0]
        file.pop(0)
        if by_number:
            m = 0
            while m < len(headers):
                if file[0][m].isdigit():
                    file[0][m] = int(file[0][m])
                elif file[0][m].replace('.', '').isdigit():
                    file[0][m] = float(file[0][m])
                else:
                    if file[0][m] == 'True' or file[0][m] == 'False':
                        file[0][m] = bool(file[0][m])
                my_list[str(m)] = type(file[0][m])
                m += 1
        else:
            m = 0
            while m < len(headers):
                if file[0][m].isdigit():
                    file[0][m] = int(file[0][m])
                elif file[0][m].replace('.', '').isdigit():
                    file[0][m] = float(file[0][m])
                else:
                    if file[0][m] == 'True' or file[0][m] == 'False':
                        file[0][m] = bool(file[0][m])
                my_list[headers[m]] = type(file[0][m])
                m += 1
        # csv_module.save_table(output_directory, my_list.keys(), my_list.values())
        # print(my_list)
        return my_list
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')


def set_column_types(file_name, types_dict='str', by_number=True):
    # output_directory = '/home/olya/Рабочий стол/python/set_column_types.csv'
    types = ['int', 'float', 'bool', 'str']
    my_list = {}
    try:
        assert types_dict in types, 'Неправильно задано значение аргумента types_dict'
    except AssertionError as e:
        print(e)
    try:
        file = csv_module.load_table(file_name)
        headers = file[0]
        file.pop(0)
        m = 0
        try:
            while m < len(headers):
                if types_dict == 'int':
                    if str(file[0][m]).isdigit():
                        file[0][m] = int(file[0][m])
                    else:
                        if file[0][m] == 'True':  #########
                            file[0][m] = 1
                        else:
                            file[0][m] = 0
                elif types_dict == 'float':
                    if str(file[0][m]).replace('.', '').isdigit():
                        file[0][m] = float(file[0][m])
                    else:
                        if file[0][m] == 'True':
                            file[0][m] = 1.0
                        else:
                            file[0][m] = 0.0
                elif types_dict == 'bool':
                    file[0][m] = bool(file[0][m])
                elif types_dict == 'str':
                    file[0][m] = str(file[0][m])
                if by_number:
                    my_list[str(m)] = str(type(file[0][m]))
                    m += 1
                else:
                    my_list[headers[m]] = str(type(file[0][m]))
                    m += 1
        except IndexError:
            print('Проблема с индексом в set_column_types')
        # csv_module.save_table(output_directory, my_list.keys(), my_list.values())
        print(my_list)
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')


def get_values(file_name, column=0):
    # output_directory = '/home/olya/Рабочий стол/python/get_values.csv'
    arr = []
    try:
        file = csv_module.load_table(file_name)
        headers = file[0]
        file.pop(0)
        if type(column) == str:
            operand = headers.index(column)
            for row in file:
                arr.append([row[operand]])
                print(row[operand])
        elif type(column) == int:
            for row in file:
                arr.append([row[column]])
                print(row[column])
    except IndexError:
        print('Проблемы с индексом в get_values')
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')
    # csv_module.save_table(output_directory, *arr)


def get_value(file_name, column=0):
    # output_directory = '/home/olya/Рабочий стол/python/get_value.csv'
    result = ''
    try:
        file = csv_module.load_table(file_name)
        headers = file[0]
        file.pop(0)
        if type(column) == str:
            operand = headers.index(column)
            result = file[0][operand]
            print(result)
        elif type(column) == int:
            result = file[0][column]
            print(result)
    except IndexError:
        print('Проблемы с индексом в get_value')
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')
    # csv_module.save_table(output_directory, [result])


def set_values(file_name, values, column=0):
    # output_directory = '/home/olya/Рабочий стол/python/set_values.csv'
    arr = []
    try:
        file = csv_module.load_table(file_name)
        headers = file[0]
        file.pop(0)
        for i in file:
            arr.append(i)
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')
    if type(column) == str:
        operand = headers.index(column)
        for row in arr:
            row[operand] = values
    elif type(column) == int:
        for row in arr:
            row[column] = values
    for i in arr:
        print(i)
    # csv_module.save_table(output_directory, *arr)


def set_value(file_name, value, column=0):
    output_directory = '/home/olya/Рабочий стол/python/set_value.csv'
    arr = []
    try:
        file = csv_module.load_table(file_name)
        headers = file[0]
        file.pop(0)
        for i in file:
            arr.append(i)
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')
    if type(column) == str:
        operand = headers.index(column)
        arr[0][operand] = value
    elif type(column) == int:
        arr[0][column] = value
    for i in arr:
        print(i)
    csv_module.save_table(output_directory, *arr)


def print_table(file_name):
    try:
        file = csv_module.load_table(file_name)
        table = PrettyTable()
        table.field_names = file[0]
        file.pop(0)
        table.add_rows(file)
        print(table)
        return table
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')
