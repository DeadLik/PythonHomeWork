from HomeWork_OOP7.ActionClass.ActionAnimal import ActionAnimal
from HomeWork_OOP7.Animals.Animals import Animals


class Cat(Animals, ActionAnimal):

    def __init__(self, view: str, name: str, color: str, gender: str, age: int, weight: int):
        super().__init__(view, name, color, gender, age, weight)

    def voice(self):
        return 'Mяу, Мяу'

    def __str__(self):
        return f'Кот(' \
               f'порода = {self._view}, ' \
               f'имя = {self._name}, ' \
               f'цвет = {self._color}, ' \
               f'пол = {self._gender}, ' \
               f'возраст = {self._age}, ' \
               f'вес = {self._weight}' \
               f')'
