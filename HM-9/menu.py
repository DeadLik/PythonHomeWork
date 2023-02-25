from phoneBook import PhoneBook


class Menu:
    def __init__(self, path):
        print('Телефонный справочник')
        print('Введите команду:\n'
              '1. Открыть файл\n'
              '2. Выход')
        self.path = path
        openCommand = input('-> ')
        if openCommand == '1':
            document = PhoneBook(self.path)
            while True:
                print()
                print('Введите команду:\n'
                      '1. Сохранить файл\n'
                      '2. Показать контакты\n'
                      '3. Добавить контакт\n'
                      '4. Изменить контакт\n'
                      '5. Найти контакт\n'
                      '6. Удалить контакт\n'
                      '7. Выход')
                command = input('-> ')
                if command == '1':
                    print()
                    document.save_file(self.path)
                elif command == '2':
                    print()
                    document.show_file()
                elif command == '3':
                    print()
                    document.add_contact()
                elif command == '4':
                    print()
                    document.change_contact()
                elif command == '5':
                    print()
                    document.find_contact()
                elif command == '6':
                    print()
                    document.del_con()
                elif command == '7':
                    print()
                    print('Сохранить файл перед выходом?\n'
                          '1. Да\n'
                          '2. Нет')
                    option = input('-> ')
                    if option == '1':
                        document.save_file(self.path)
                        break
                    elif option == '2':
                        break
                    else:
                        print()
                        print('Вы ввели неверную команду, повторите попытку')
                        continue
