import logging

logging.basicConfig(filename='phonebook.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s:%(message)s',
                    encoding='utf-8')


class PhoneBook:

    def __init__(self, path: str = 'phone_db.txt'):
        self.path = path
        self.phone_book = []
        logging.info('PhoneBook объект создан')

    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        for contact in data:
            pb = {}
            new = contact.strip().split(';')
            pb['name'] = new[0]
            pb['phone'] = new[1]
            pb['comment'] = new[2]
            self.phone_book.append(pb)
        print('Телефонная книга успешно загружена!')

    def save_file(self):
        with open(self.path, 'w', encoding='UTF-8') as file:
            for contact in self.phone_book:
                file.write(f"{contact['name']};{contact['phone']};{contact['comment']}\n")
        print('Телефонная книга успешно сохранена!')

    def get(self):
        return self.phone_book

    def new_contact(self, contact: dict):
        self.phone_book.append(contact)
        logging.info(f'Контакт {contact.get("name")} успешно записан!')

    def search(self, word: str) -> list:
        search_result = []
        for contact in self.phone_book:
            for field in contact.values():
                if word in field:
                    search_result.append(contact)
        return search_result

    def change(self, i: int, new_value: dict):
        self.phone_book[i] = new_value
        logging.info(f'Изменен контакт {new_value.get("name")}')

    def delete(self, i: int):
        try:
            contact = self.phone_book.pop(i)
            logging.info(f'Контакт {contact.get("name")} успешно удален!')
        except IndexError:
            logging.exception('Ошибка, данного контакта нет в списке')
            print('\nОшибка, данного контакта нет в списке\n')
