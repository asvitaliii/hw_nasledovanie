from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

from models import *

animal = None
bird = None
pinguin = None


class Manager(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.__win = uic.loadUi('gui.ui')

    def __set_slots(self):
        self.__win.push_animal_create.clicked.connect(self.__animal_create)
        self.__win.push_animal_rename.clicked.connect(self.__animal_rename)
        self.__win.push_animal_number_change.clicked.connect(self.__animal_number_change)
        self.__win.push_animal_rb_status_change.clicked.connect(self.__animal_rb_status_change)
        self.__win.push_animal_live.clicked.connect(self.__animal_live)
        self.__win.push_animal_showinfo.clicked.connect(self.__animal_showinfo)

        self.__win.push_bird_create.clicked.connect(self.__bird_create)
        self.__win.push_bird_rename.clicked.connect(self.__bird_rename)
        self.__win.push_bird_number_change.clicked.connect(self.__bird_number_change)
        self.__win.push_bird_rb_status_change.clicked.connect(self.__bird_rb_status_change)
        self.__win.push_bird_predator_status_change.clicked.connect(self.__bird_predator_status_change)
        self.__win.push_bird_live.clicked.connect(self.__bird_live)
        self.__win.push_bird_fly.clicked.connect(self.__bird_fly)
        self.__win.push_bird_showinfo.clicked.connect(self.__bird_showinfo)

        self.__win.push_pinguin_create.clicked.connect(self.__pinguin_create)
        self.__win.push_pinguin_rename.clicked.connect(self.__pinguin_rename)
        self.__win.push_pinguin_number_change.clicked.connect(self.__pinguin_number_change)
        self.__win.push_pinguin_rb_status_change.clicked.connect(self.__pinguin_rb_status_change)
        self.__win.push_pinguin_predator_status_change.clicked.connect(self.__pinguin_predator_status_change)
        self.__win.push_pinguin_living_place_change.clicked.connect(self.__pinguin_living_place_change)
        self.__win.push_pinguin_live.clicked.connect(self.__pinguin_live)
        self.__win.push_pinguin_fly.clicked.connect(self.__pinguin_fly)
        self.__win.push_pinguin_showinfo.clicked.connect(self.__pinguin_showinfo)

    def show(self):
        self.__set_slots()
        self.__win.show()

    def __animal_create(self):
        global animal
        animal = Animal(self.__win.line_name.text(), self.__win.line_number.text(), self.__win.line_red_book.text())

    def __animal_rename(self):
        animal.set_name(self.__win.line_name.text())

    def __animal_number_change(self):
        animal.set_number(self.__win.line_number.text())

    def __animal_rb_status_change(self):
        animal.set_red_boobk_status(self.__win.line_red_book.text())

    def __animal_live(self):
        animal.living()

    def __animal_showinfo(self):
        QMessageBox.information(self, 'Инфо о животных:', f'{animal}')
        # print(animal)

    def __bird_create(self):
        global bird
        bird = Bird(self.__win.line_name.text(), self.__win.line_number.text(), self.__win.line_red_book.text(),
                    self.__win.line_predator.text())

    def __bird_rename(self):
        bird.set_name(self.__win.line_name.text())

    def __bird_number_change(self):
        bird.set_number(self.__win.line_number.text())

    def __bird_rb_status_change(self):
        bird.set_red_book_status(self.__win.line_red_book.text())

    def __bird_predator_status_change(self):
        bird.set_hunting_status(self.__win.line_predator.text())

    def __bird_live(self):
        bird.living()

    def __bird_fly(self):
        bird.flying()

    def __bird_showinfo(self):
        QMessageBox.information(self, 'Инфо о птицах:', f'{bird}')
        # print(bird)

    def __pinguin_create(self):
        global pinguin
        pinguin = Pinguin(self.__win.line_name.text(), self.__win.line_number.text(), self.__win.line_red_book.text(),
                          self.__win.line_living_place.text(), self.__win.line_predator.text())

    def __pinguin_rename(self):
        pinguin.set_name(self.__win.line_name.text())

    def __pinguin_number_change(self):
        pinguin.set_number(self.__win.line_number.text())

    def __pinguin_rb_status_change(self):
        pinguin.set_red_book_status(self.__win.line_red_book.text())

    def __pinguin_predator_status_change(self):
        pinguin.set_hunting_status(self.__win.line_predator.text())

    def __pinguin_living_place_change(self):
        pinguin.set_living_place(self.__win.line_living_place.text())

    def __pinguin_live(self):
        pinguin.living()

    def __pinguin_fly(self):
        pinguin.flying()

    def __pinguin_showinfo(self):
        QMessageBox.information(self, 'Инфо о пингвинах:', f'{pinguin}')
        # print(pinguin)
