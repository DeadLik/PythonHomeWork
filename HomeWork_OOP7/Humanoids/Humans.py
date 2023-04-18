class Humans:

    def __init__(self, name: str, status: str, gender: str, age: int):
        self._name = name
        self._status = status
        self._gender = gender
        self._age = age

    def get_name(self) -> str:
        return self._name

    def get_status(self) -> str:
        return self._status

    def get_gender(self) -> str:
        return self._gender

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int):
        self._age = new_age