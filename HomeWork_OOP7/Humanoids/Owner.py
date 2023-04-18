from HomeWork_OOP7.ActionClass.ActionHuman import ActionHuman
from HomeWork_OOP7.Humanoids.Humans import Humans


class Owner(Humans, ActionHuman):

    def __init__(self, name: str, status: str, gender: str, age: int):
        super().__init__(name, status, gender, age)

    def __str__(self):
        return f'Хозяин(' \
               f'имя = {self._name}, ' \
               f'должность = {self._status}, ' \
               f'пол = {self._gender}, ' \
               f'возраст = {self._age}, ' \
               f')'

    def action(self):
        return 'Привел/а на обследование своего питомца'



