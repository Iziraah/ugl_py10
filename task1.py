# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.


class Animal:
    def __init__(self, name, age):
        self.__name, self.__age = name, age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class Fish(Animal):
    def __imit__(self, name, age, color):
        super().__init__(name, age)
        self.__color = color

    def get_specific(self):
        return self.__color


class Mammal(Animal):
    def __init__(self, name, age, wool):
        super().__init__(name, age)
        self.__wool = wool

    def get_specific(self):
        return self.__wool


class Bird(Animal):
    def __init__(self, name, age, feather):
        super().__init__(name, age)
        self.__feather = feather

    def get_specific(self):
        return self.__feather


class Fabrika(Bird):
    def __init__(self, name, age, feather, type):
        super().__init__(name, age, feather)
        self.__type = type

    def get_type(self):
        return self.__type


fabr = Fabrika("Dyatel", 2, "Black", "Bird")
print(fabr.get_specific(), fabr.get_type())
