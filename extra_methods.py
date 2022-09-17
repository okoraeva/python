import csv_module
import methods
''' 
Сложности:
    6) Добавить набор функций add, sub, mul, div, которые обеспечат выполнение арифмитических операций для столбцов типа
     int, float, bool. Продумать сигнатуру функций и изменения в другие функции, которые позволят удобно выполнять 
     арифметические операции со столбцами и присваивать результаты выч. Реализовать реагирование на некорректные 
     значения с помощью генерации исключительных ситуаций.
Сложность 2
    7) По аналогии с п. 6 реализовать функции eq (==), gr (>), ls (<), ge (>=), le (<=), ne (==), которые возвращают 
    список булевских значений длинной в количество строк сравниваемых столбцов. Реализовать функцию filter_rows 
    (bool_list, copy_table=False) – получение новой таблицы из строк для которых в bool_list (длинной в количество 
    строк в таблице) находится значение True.
Сложность 3
    8) Реализовать функцию merge_tables(table1, table2, by_number=True): в результате слияния создается таблица с 
    набором столбцов, соответствующих объединенному набору столбцов исходных таблиц. Соответствие строк ищется либо по 
    их номеру (by_number=True) либо по значению индекса (1й столбец). При выполнении слияния возможно множество 
    конфликтных ситуаций. Автор должен их описать и определить допустимый способ реакции на них (в т.ч. через 
    дополнительные параметры функции и инициацию исключительных ситуаций).
Сложность 2
'''


def merge_tables(table1, table2):
    output_directory = '/home/olya/Рабочий стол/python/merge.csv'
    arr1 = []
    arr2 = []
    try:
        file1 = csv_module.load_table(table1)
        headers1 = file1[0]
        file1.pop(0)
        for i in file1:
            arr1.append(i)
        file2 = csv_module.load_table(table2)
        headers2 = file2[0]
        file2.pop(0)
        for i in file2:
            arr2.append(i)
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')
    headers = headers1 + headers2
    arr = []
    try:
        if len(arr1) > len(arr2):
            max_leng = len(arr1)
        else:
            max_leng = len(arr2)
        i = 0
        while i < max_leng:
            merge = []
            if arr1[i]:
                merge.append(arr1[i])
            if arr2[i]:
                merge.append(arr2[i])
            flatten_list = []
            for el in merge:
                for item in el:
                    flatten_list.append(item)
            arr.append(flatten_list)
            i += 1
    except IndexError:
        print('Проблема с индексом в merge_tables')
    print(headers)
    for i in arr:
        print(i)
    csv_module.save_table(output_directory, headers, *arr)


def add(file_name, column1, column2):
    output_directory = '/home/olya/Рабочий стол/python/add.csv'
    try:
        file = csv_module.load_table(file_name)
        headers = file[0]
        file.pop(0)
        types = methods.get_column_types(file_name)
        arr = []
        for i in types.values():
            arr.append(i)
        type1 = arr[column1]
        type2 = arr[column2]
        compound = []
        try:
            if type1 == type2:
                for i in file:
                    if type1 == int:
                        compound.append(int(i[column1]) + int(i[column2]))
                    elif type1 == float:
                        compound.append(float(i[column1]) + float(i[column2]))
                    else:
                        if i[column1] == 'False' or i[column1] == 'false' or i[column1] == 'None':
                            i[column1] = 0
                        if i[column2] == 'False' or i[column2] == 'false' or i[column2] == 'None':
                            i[column2] = 0
                        compound.append(bool(i[column1]) + bool(i[column2]))
                print(compound)
        except ValueError:
            print('Ошибка вычислений в add')
        except IndexError:
            print('Ошибка индекса в add')
        headers.pop(column2)
        headers[column1] = 'Sum'
        m = 0
        while m < len(file):
            file[m][column1] = compound[m]
            file[m].pop(column2)
            m += 1
        csv_module.save_table(output_directory, headers, *file)
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')


def sub(file_name, column1, column2):
    output_directory = '/home/olya/Рабочий стол/python/sub.csv'
    try:
        file = csv_module.load_table(file_name)
        headers = file[0]
        file.pop(0)
        types = methods.get_column_types(file_name)
        arr = []
        for i in types.values():
            arr.append(i)
        type1 = arr[column1]
        type2 = arr[column2]
        compound = []
        try:
            if type1 == type2:
                for i in file:
                    if type1 == int:
                        compound.append(int(i[column1]) - int(i[column2]))
                    elif type1 == float:
                        compound.append(float(i[column1]) - float(i[column2]))
                    else:
                        if i[column1] == 'False' or i[column1] == 'false' or i[column1] == 'None':
                            i[column1] = 0
                        if i[column2] == 'False' or i[column2] == 'false' or i[column2] == 'None':
                            i[column2] = 0
                        compound.append(bool(i[column1]) - bool(i[column2]))
                print(compound)
        except ValueError:
            print('Ошибка вычислений в sub')
        except IndexError:
            print('Ошибка индекса в sub')
        headers.pop(column2)
        headers[column1] = 'Sub'
        m = 0
        while m < len(file):
            file[m][column1] = compound[m]
            file[m].pop(column2)
            m += 1
        csv_module.save_table(output_directory, headers, *file)
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')


def mul(file_name, column1, column2):
    output_directory = '/home/olya/Рабочий стол/python/mul.csv'
    try:
        file = csv_module.load_table(file_name)
        headers = file[0]
        file.pop(0)
        types = methods.get_column_types(file_name)
        arr = []
        for i in types.values():
            arr.append(i)
        type1 = arr[column1]
        type2 = arr[column2]
        compound = []
        try:
            if type1 == type2:
                for i in file:
                    if type1 == int:
                        compound.append(int(i[column1]) * int(i[column2]))
                    elif type1 == float:
                        compound.append(float(i[column1]) * float(i[column2]))
                    else:
                        if i[column1] == 'False' or i[column1] == 'false' or i[column1] == 'None':
                            i[column1] = 0
                        if i[column2] == 'False' or i[column2] == 'false' or i[column2] == 'None':
                            i[column2] = 0
                        compound.append(bool(i[column1]) * bool(i[column2]))
                print(compound)
        except ValueError:
            print('Ошибка вычислений в mul')
        except IndexError:
            print('Ошибка индекса в mul')
        headers.pop(column2)
        headers[column1] = 'Multiply'
        m = 0
        while m < len(file):
            file[m][column1] = compound[m]
            file[m].pop(column2)
            m += 1
        csv_module.save_table(output_directory, headers, *file)
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')


def div(file_name, column1, column2):
    output_directory = '/home/olya/Рабочий стол/python/div.csv'
    try:
        file = csv_module.load_table(file_name)
        headers = file[0]
        file.pop(0)
        types = methods.get_column_types(file_name)
        arr = []
        for i in types.values():
            arr.append(i)
        type1 = arr[column1]
        type2 = arr[column2]
        compound = []
        try:
            if type1 == type2:
                for i in file:
                    if type1 == int:
                        compound.append(int(i[column1]) / int(i[column2]))
                    elif type1 == float:
                        compound.append(float(i[column1]) / float(i[column2]))
                    else:
                        if i[column1] == 'False' or i[column1] == 'false' or i[column1] == 'None':
                            i[column1] = 0
                        if i[column2] == 'False' or i[column2] == 'false' or i[column2] == 'None':
                            i[column2] = 0
                        compound.append(bool(i[column1]) / bool(i[column2]))
                print(compound)
            headers.pop(column2)
            headers[column1] = 'Divide'
            m = 0
            while m < len(file):
                file[m][column1] = compound[m]
                file[m].pop(column2)
                m += 1
            csv_module.save_table(output_directory, headers, *file)
        except ValueError:
            print('Ошибка вычислений в div')
        except IndexError:
            print('Ошибка индекса в div')
        except ZeroDivisionError:
            print('Деление на ноль')
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')


def equal(file_name, column1, column2):
    output_directory = '/home/olya/Рабочий стол/python/equal.csv'
    try:
        file = csv_module.load_table(file_name)
        headers = file[0]
        file.pop(0)
        types = methods.get_column_types(file_name)
        arr = []
        for i in types.values():
            arr.append(i)
        type1 = arr[column1]
        type2 = arr[column2]
        compound = []
        try:
            if type1 == type2:
                for i in file:
                    if type1 == int:
                        compound.append(int(i[column1]) == int(i[column2]))
                    elif type1 == float:
                        compound.append(float(i[column1]) == float(i[column2]))
                    else:
                        if i[column1] == 'False' or i[column1] == 'false' or i[column1] == 'None':
                            i[column1] = 0
                        if i[column2] == 'False' or i[column2] == 'false' or i[column2] == 'None':
                            i[column2] = 0
                        compound.append(bool(i[column1]) == bool(i[column2]))
                print(compound)
            headers.pop(column2)
            headers[column1] = 'Equal'
            m = 0
            while m < len(file):
                file[m][column1] = compound[m]
                file[m].pop(column2)
                m += 1
            csv_module.save_table(output_directory, headers, *file)
        except ValueError:
            print('Ошибка вычислений в equal')
        except IndexError:
            print('Ошибка индекса в equal')
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')


def greater(file_name, column1, column2):
    output_directory = '/home/olya/Рабочий стол/python/greater.csv'
    try:
        file = csv_module.load_table(file_name)
        headers = file[0]
        file.pop(0)
        types = methods.get_column_types(file_name)
        arr = []
        for i in types.values():
            arr.append(i)
        type1 = arr[column1]
        type2 = arr[column2]
        compound = []
        try:
            if type1 == type2:
                for i in file:
                    if type1 == int:
                        compound.append(int(i[column1]) > int(i[column2]))
                    elif type1 == float:
                        compound.append(float(i[column1]) > float(i[column2]))
                    else:
                        if i[column1] == 'False' or i[column1] == 'false' or i[column1] == 'None':
                            i[column1] = 0
                        if i[column2] == 'False' or i[column2] == 'false' or i[column2] == 'None':
                            i[column2] = 0
                        compound.append(bool(i[column1]) > bool(i[column2]))
                print(compound)
            headers.pop(column2)
            headers[column1] = 'Greater'
            m = 0
            while m < len(file):
                file[m][column1] = compound[m]
                file[m].pop(column2)
                m += 1
            csv_module.save_table(output_directory, headers, *file)
        except ValueError:
            print('Ошибка вычислений в greater')
        except IndexError:
            print('Ошибка индекса в greater')
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')


def less(file_name, column1, column2):
    output_directory = '/home/olya/Рабочий стол/python/less.csv'
    try:
        file = csv_module.load_table(file_name)
        headers = file[0]
        file.pop(0)
        types = methods.get_column_types(file_name)
        arr = []
        for i in types.values():
            arr.append(i)
        type1 = arr[column1]
        type2 = arr[column2]
        compound = []
        try:
            if type1 == type2:
                for i in file:
                    if type1 == int:
                        compound.append(int(i[column1]) < int(i[column2]))
                    elif type1 == float:
                        compound.append(float(i[column1]) < float(i[column2]))
                    else:
                        if i[column1] == 'False' or i[column1] == 'false' or i[column1] == 'None':
                            i[column1] = 0
                        if i[column2] == 'False' or i[column2] == 'false' or i[column2] == 'None':
                            i[column2] = 0
                        compound.append(bool(i[column1]) < bool(i[column2]))
                print(compound)
            headers.pop(column2)
            headers[column1] = 'Less'
            m = 0
            while m < len(file):
                file[m][column1] = compound[m]
                file[m].pop(column2)
                m += 1
            csv_module.save_table(output_directory, headers, *file)
        except ValueError:
            print('Ошибка вычислений в less')
        except IndexError:
            print('Ошибка индекса в less')
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')


def greater_or_eq(file_name, column1, column2):
    output_directory = '/home/olya/Рабочий стол/python/greater_or_eq.csv'
    try:
        file = csv_module.load_table(file_name)
        headers = file[0]
        file.pop(0)
        types = methods.get_column_types(file_name)
        arr = []
        for i in types.values():
            arr.append(i)
        type1 = arr[column1]
        type2 = arr[column2]
        compound = []
        try:
            if type1 == type2:
                for i in file:
                    if type1 == int:
                        compound.append(int(i[column1]) >= int(i[column2]))
                    elif type1 == float:
                        compound.append(float(i[column1]) >= float(i[column2]))
                    else:
                        if i[column1] == 'False' or i[column1] == 'false' or i[column1] == 'None':
                            i[column1] = 0
                        if i[column2] == 'False' or i[column2] == 'false' or i[column2] == 'None':
                            i[column2] = 0
                        compound.append(bool(i[column1]) >= bool(i[column2]))
                print(compound)
            headers.pop(column2)
            headers[column1] = 'Greater_or_eq'
            m = 0
            while m < len(file):
                file[m][column1] = compound[m]
                file[m].pop(column2)
                m += 1
            csv_module.save_table(output_directory, headers, *file)
        except ValueError:
            print('Ошибка вычислений в greater_or_eq')
        except IndexError:
            print('Ошибка индекса в greater_or_eq')
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')


def less_or_eq(file_name, column1, column2):
    output_directory = '/home/olya/Рабочий стол/python/less_or_eq.csv'
    try:
        file = csv_module.load_table(file_name)
        headers = file[0]
        file.pop(0)
        types = methods.get_column_types(file_name)
        arr = []
        for i in types.values():
            arr.append(i)
        type1 = arr[column1]
        type2 = arr[column2]
        compound = []
        try:
            if type1 == type2:
                for i in file:
                    if type1 == int:
                        compound.append(int(i[column1]) <= int(i[column2]))
                    elif type1 == float:
                        compound.append(float(i[column1]) <= float(i[column2]))
                    else:
                        if i[column1] == 'False' or i[column1] == 'false' or i[column1] == 'None':
                            i[column1] = 0
                        if i[column2] == 'False' or i[column2] == 'false' or i[column2] == 'None':
                            i[column2] = 0
                        compound.append(bool(i[column1]) <= bool(i[column2]))
                print(compound)
            headers.pop(column2)
            headers[column1] = 'Less_or_eq'
            m = 0
            while m < len(file):
                file[m][column1] = compound[m]
                file[m].pop(column2)
                m += 1
            csv_module.save_table(output_directory, headers, *file)
        except ValueError:
            print('Ошибка вычислений в less_or_eq')
        except IndexError:
            print('Ошибка индекса в less_or_eq')
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')


def not_equal(file_name, column1, column2):
    output_directory = '/home/olya/Рабочий стол/python/not_equal.csv'
    try:
        file = csv_module.load_table(file_name)
        headers = file[0]
        file.pop(0)
        types = methods.get_column_types(file_name)
        arr = []
        for i in types.values():
            arr.append(i)
        type1 = arr[column1]
        type2 = arr[column2]
        compound = []
        try:
            if type1 == type2:
                for i in file:
                    if type1 == int:
                        compound.append(int(i[column1]) != int(i[column2]))
                    elif type1 == float:
                        compound.append(float(i[column1]) != float(i[column2]))
                    else:
                        if i[column1] == 'False' or i[column1] == 'false' or i[column1] == 'None':
                            i[column1] = 0
                        if i[column2] == 'False' or i[column2] == 'false' or i[column2] == 'None':
                            i[column2] = 0
                        compound.append(bool(i[column1]) != bool(i[column2]))
                print(compound)
            headers.pop(column2)
            headers[column1] = 'Not_equal'
            m = 0
            while m < len(file):
                file[m][column1] = compound[m]
                file[m].pop(column2)
                m += 1
            csv_module.save_table(output_directory, headers, *file)
        except ValueError:
            print('Ошибка вычислений в not_equal')
        except IndexError:
            print('Ошибка индекса в not_equal')
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')


def filter_rows(file_name, bool_list, copy_table=False):
    output_directory = '/home/olya/Рабочий стол/python/filter_rows.csv'
    arr = []
    try:
        file = csv_module.load_table(file_name)
        headers = file[0]
        file.pop(0)
        for i in file:
            if i[bool_list] == 'True':
                arr.append(i)
    except IndexError:
            print('Ошибка индекса в filter_rows')
    except IOError:
        print('Попытка получения доступа к несуществующему файлу')
    if copy_table:
        csv_module.save_table(output_directory, headers, *arr)
    for i in arr:
        print(i)
