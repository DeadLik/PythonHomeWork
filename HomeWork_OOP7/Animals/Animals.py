from HomeWork_OOP7.ActionClass.ActionAnimal import ActionAnimal


class Animals(ActionAnimal):

    def __init__(self, view: str, name: str, color: str, gender: str, age: int, weight: int):
        self._view = view
        self._name = name
        self._color = color
        self._gender = gender
        self._age = age
        self._weight = weight

    def get_view(self) -> str:
        return self._view

    def set_view(self, new_view: str):
        self._view = new_view

    def get_name(self) -> str:
        return self._name

    def set_name(self, new_name: str):
        self._name = new_name

    def get_color(self) -> str:
        return self._color

    def get_gender(self) -> str:
        return self._gender

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int):
        self._age = new_age

    def get_weight(self) -> int:
        return self._weight

    def set_weight(self, new_weight: int):
        self._weight = new_weight

    def voice(self) -> str:
        return super().voice()

