phone_book = []


def open_file():
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        phone_book = file.readlines()
        print('Файл открыт')
        return phone_book


def save_file():
    with open('phone_book.txt', 'w', encoding='utf-8') as file:
        for i in phone_book:
            file.write(i)
        print('Файл сохранён')


def show_file():
    for i in enumerate(phone_book):
        print(i)


def add_contact():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    middle_name = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    contact = ' '.join([last_name, first_name, middle_name + ':', phone_number])
    phone_book.append('\n' + contact)


def change_contact():
    contact = int(input('Введите номер контакта, которого вы хотите изменить: '))
    for i in range(len(phone_book)):
        if i == contact:
            print()
            print(f'Вы меняете контакт {phone_book[i]}')
            print('Хотите его изменить?\n'
                  '1. Да\n'
                  '2. Нет')
            option = input()
            if option == '1':
                last_name = input('Введите новую фамилию: ')
                first_name = input('Введите новое имя: ')
                middle_name = input('Введите новое отчество: ')
                phone_number = input('Введите новый номер телефона: ')
                contact_new = ' '.join([last_name, first_name, middle_name + ':', phone_number])
                phone_book[i] = contact_new + '\n'
                break
            elif option == '2':
                break
            else:
                break
    else:
        print('Данного контакта нет в списке')


def find_contact():
    contact = int(input('Введите номер контакта для поиска: '))
    for i in range(len(phone_book)):
        if i == contact:
            print(phone_book[i])
            break
    else:
        print('Данного контакта нет в списке')


def del_con():
    contact = int(input('Введите номер контакта для удаления: '))
    for i in range(len(phone_book)):
        if i == contact:
            print()
            print(f'Вы хотите удалить контакт {phone_book[i]}')
            print('Удалить?\n'
                  '1. Да\n'
                  '2. Нет')
            option = input()
            if option == '1':
                phone_book.pop(i)
                break
            elif option == '2':
                break
            else:
                break
    else:
        print('Данного контакта нет в списке')
