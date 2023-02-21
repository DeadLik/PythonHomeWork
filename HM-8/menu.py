import phoneBook as ph


def menu():
    print('Телефонный справочник')
    print('Введите команду:\n'
          '1. Открыть файл\n'
          '2. Выход')
    openCommand = input('-> ')
    if openCommand == '1':
        ph.phone_book = ph.open_file()
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
                ph.save_file()
            elif command == '2':
                print()
                ph.show_file()
            elif command == '3':
                print()
                ph.add_contact()
            elif command == '4':
                print()
                ph.change_contact()
            elif command == '5':
                print()
                ph.find_contact()
            elif command == '6':
                print()
                ph.del_con()
            elif command == '7':
                print()
                print('Сохранить файл перед выходом?\n'
                      '1. Да\n'
                      '2. Нет')
                option = input('-> ')
                if option == '1':
                    ph.save_file()
                    break
                elif option == '2':
                    break
                else:
                    break
