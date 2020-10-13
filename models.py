class Animal(object):
    def __init__(self, name: str, number: int, red_book: str):
        self._name = name
        self._number = number
        if red_book == 'да':
            self._red_book = True
        else:
            self._red_book = False

    def __str__(self):
        if self._red_book:
            return f"{self._name} в количестве {self._number} штук, исчезающий вид!"
        else:
            return f"{self._name} в количестве {self._number} штук."

    def set_name(self, name):
        self._name = name

    def set_number(self, number):
        if self._number < number:
            self._number = number
        elif not self._red_book:
            self._number = number
        else:
            print("Нельзя уменшать количество, этот вид под защитой!")

    def set_red_book_status(self, red_book: str):
        if red_book == 'да':
            self._red_book = True
        else:
            self._red_book = False

    def living(self):
        print(f"{self._name} живет в зоопарке!")


class Bird(Animal):
    def __init__(self, name: str, number: int, red_book: str, predator: str):
        super().__init__(name, number, red_book)
        if predator == 'да':
            self._predator = True
        else:
            self._predator = False

    def __str__(self):
        if self._predator:
            return super().__str__()+' Хищник.'
        else:
            return super().__str__()

    def set_hunting_status(self, predator: str):
        if predator == 'да':
            self._predator = True
        else:
            self._predator = False

    def flying(self):
        print(f'{self._name} летает!')


class Pinguin(Bird):
    def __init__(self, name: str, number: int, red_book: str, living_place: str, predator='да'):
        super().__init__(name, number, red_book, predator)
        self._living_place = living_place

    def __str__(self):
        return super().__str__()+f' Место обитания - {self._living_place}'

    def set_living_place(self, living_place):
        self._living_place = living_place

    def flying(self):
        print(f"{self._name} не летает, он плавает!")
