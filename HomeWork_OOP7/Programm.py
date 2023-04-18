import random
import time

from HomeWork_OOP7.Animals.Cat import Cat
from HomeWork_OOP7.Animals.Dog import Dog
from HomeWork_OOP7.Animals.Pig import Pig
from HomeWork_OOP7.Helpers.Numbers import Numbers
from HomeWork_OOP7.Humanoids.Doctor import Doctor
from HomeWork_OOP7.Humanoids.Owner import Owner

doctor = Doctor('Артём', 'Ветеринар', 'Мужской', Numbers.set_random(25))

owner1 = Owner('Антон', 'Менеджер', 'Мужской', Numbers.set_random(25))
owner2 = Owner('Боб', 'Директор', 'Мужской', Numbers.set_random(25))
owner3 = Owner('Света', 'Продавец', 'Женский', Numbers.set_random(25))
owner4 = Owner('Коля', 'Маркетолог', 'Мужской', Numbers.set_random(25))
owner5 = Owner('Елена', 'Юрист', 'Женский', Numbers.set_random(25))

cat = Cat('Персидский', 'Мира', 'Коричневый', 'Женский', Numbers.set_random(2), Numbers.set_random(5))
cat1 = Cat('Шотландский', 'Роза', 'Рыжий', 'Женский', Numbers.set_random(2), Numbers.set_random(5))

pig = Pig('Карликовая', 'Ненси', 'Серый', 'Женский', Numbers.set_random(2), Numbers.set_random(5))

dog = Dog('Терьер', 'Борзый', 'Черный', 'Мужской', Numbers.set_random(2), Numbers.set_random(5))
dog1 = Dog('Спаниель', 'Капер', 'Белый', 'Мужской', Numbers.set_random(2), Numbers.set_random(5))

listAnimal = [cat, cat1, pig, dog, dog1]
listOwner = [owner1, owner2, owner3, owner4, owner5]

for i in range(len(listAnimal)) and range(len(listOwner)):
    rand: int = random.randint(0, 4)
    print()
    time.sleep(1)
    print(f'{listOwner[rand]} {listOwner[rand].action()}: {listAnimal[rand]}')
    print(f'{listAnimal[rand]} {listAnimal[rand].voice()}')
    print(f'{doctor} {doctor.action()}: {listAnimal[rand]}')
    time.sleep(1)
    print(f'{doctor.treatment()}: {listAnimal[rand]}')
    print()
