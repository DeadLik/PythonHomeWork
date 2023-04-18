import random

from HomeWork_OOP7.ActionClass.ActionHuman import ActionHuman
from HomeWork_OOP7.Humanoids.Humans import Humans


class Doctor(Humans, ActionHuman):

    def __init__(self, name: str, status: str, gender: str, age: int):
        super().__init__(name, status, gender, age)

    def __str__(self):
        return f'Доктор(' \
               f'имя = {self._name}, ' \
               f'должность = {self._status}, ' \
               f'пол = {self._gender}, ' \
               f'возраст = {self._age}, ' \
               f')'

    def action(self):
        return 'Обследует животное'

    def treatment(self):
        rnd = random.randint(1, 3)

        match rnd:
            case 1:
                return f'{self.get_name()}: сделал укол'
            case 2:
                return f'{self.get_name()}: дал таблетку'
            case 3:
                return f'{self.get_name()}: животное здорово'
