import pickle


def load_table(file_name):
    directory = open(file_name, 'rb')
    file = pickle.load(directory)
    print(file)


def save_table(file_name):
    directory = open('/home/olya/Рабочий стол/python/out_pickle.pickle', 'wb')
    pickle.dump(file_name, directory)
