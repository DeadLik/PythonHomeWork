class PhoneBook:
    phone_book = []

    def __init__(self, path):
        self.path = path
        with open(path, 'r', encoding='utf-8') as file:
            self.phone_book = file.readlines()
            print('Файл открыт')

    def save_file(self, path):
        self.path = path
        with open(path, 'w', encoding='utf-8') as file:
            for i in self.phone_book:
                file.write(i)
            print('Файл сохранён')

    def show_file(self):
        for i in enumerate(self.phone_book):
            print(i)

    def add_contact(self):
        last_name = input('Введите фамилию: ')
        first_name = input('Введите имя: ')
        middle_name = input('Введите отчество: ')
        phone_number = input('Введите номер телефона: ')
        contact = ' '.join([last_name, first_name, middle_name + ':', phone_number])
        self.phone_book.append('\n' + contact)

    def change_contact(self):
        contact = int(input('Введите номер контакта, которого вы хотите изменить: '))
        for i in range(len(self.phone_book)):
            if i == contact:
                print()
                print(f'Вы меняете контакт {self.phone_book[i]}')
                print('Хотите его изменить?\n'
                      '1. Да\n'
                      '2. Нет')
                option = input('-> ')
                if option == '1':
                    last_name = input('Введите новую фамилию: ')
                    first_name = input('Введите новое имя: ')
                    middle_name = input('Введите новое отчество: ')
                    phone_number = input('Введите новый номер телефона: ')
                    contact_new = ' '.join([last_name, first_name, middle_name + ':', phone_number])
                    self.phone_book[i] = contact_new + '\n'
                    break
                elif option == '2':
                    break
                else:
                    break
        else:
            print('Данного контакта нет в списке')

    def find_contact(self):
        contact = int(input('Введите номер контакта для поиска: '))
        for i in range(len(self.phone_book)):
            if i == contact:
                print(self.phone_book[i])
                break
        else:
            print('Данного контакта нет в списке')

    def del_con(self):
        contact = int(input('Введите номер контакта для удаления: '))
        for i in range(len(self.phone_book)):
            if i == contact:
                print()
                print(f'Вы хотите удалить контакт {self.phone_book[i]}')
                print('Удалить?\n'
                      '1. Да\n'
                      '2. Нет')
                option = input('-> ')
                if option == '1':
                    self.phone_book.pop(i)
                    break
                elif option == '2':
                    break
                else:
                    break
        else:
            print('Данного контакта нет в списке')
