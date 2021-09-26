class Wallet():
    def __init__(self, name, surname, patronymic, city, currency, balance=0, operations=[], block=0):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.city = city
        self.currency = currency
        self.balance = balance
        self.operations = operations
        self.block = block

    def blocked(self):
        self.block = 1
        return self.block

    def unblocked(self):
        self.block = 0
        return self.block

    def info(self):
        print('___Проверка баланса___')
        print('Имя владельца: ', self.name, self.surname)
        print('Баланс счёта: ', self.balance)
        print('Валюта счёта: ', self.currency)

    def add_mon(self, num):
        if self.block == 1:
            print('Карта заблокирована, нельзя совершить операцию')
        else:
            self.balance += num
            self.operations.append(f'Пополнение на {num} {self.currency}')
            print(f'Сумма пополнения: {self.balance} {self.currency}')

    def get_mon(self, num):
        if self.block == 1:
            print('Карта заблокирована, нельзя совершить операцию')
        else:
            if self.balance >= num:
                self.balance -= num
                self.operations.append(f'Снятие на {num} {self.currency}')
                print(f'Сумма снятия: {num} {self.currency}')
            else:
                print('Недостаточно денег для снятия')

    def transfer(self, obj, num):
        if self.block == 1:
            print('Карта заблокирована, нельзя совершить операцию')
        else:
            if self.balance >= num:
                obj.add_mon(num)
                self.get_mon(num)
                self.operations.pop(-1)
                self.operations.append(f'Перевод на {num} {self.currency}')
                print(f'Сумма перевода: {num} {self.currency}')
            else:
                print('Недостаточно денег для перевода')

    def show_operations(self, type):
        if type == 'все':
            print(self.operations)
        elif type == 'пополнение':
            for i in self.operations:
                if i.startswith('По'):
                    print(i)
        elif type == 'снятие':
            for i in self.operations:
                if i.startswith('С'):
                    print(i)
        elif type == 'перевод':
            for i in self.operations:
                if i.startswith('Пе'):
                    print(i)
        else:
            print('Неправильное название операции')

new_wal = Wallet('Ольга', 'Кораева', 'Георгиевна', 'Москва', 'евро')
sec_wal = Wallet('Вася', 'Пупкин', 'Анатольевич', 'Минск', 'евро')
new_wal.info()
new_wal.blocked()
new_wal.add_mon(500)
new_wal.unblocked()
new_wal.add_mon(500)
new_wal.get_mon(300)
new_wal.info()
new_wal.transfer(sec_wal, 160)
sec_wal.info()
new_wal.info()
new_wal.show_operations('все')
new_wal.show_operations('пополнение')
new_wal.show_operations('снятие')
new_wal.show_operations('перевод')
new_wal.show_operations('все')