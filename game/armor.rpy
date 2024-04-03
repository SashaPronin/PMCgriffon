init 0 python:
    class Armor(renpy.object.Object):
        def __init__(self, name,clas, def_0, def_1, mass, tipe):
            self.name = name
            self.clas = clas
            self.def_0 = def_0
            self.def_1 = def_1
            self.mass = mass
            self.tipe = tipe
default B_1=Armor("Бронежилет 1 класса", 1, 1, 5, 1, "None")
default B_2=Armor("Бронежилет 2 класса", 2, 1, 5, 1.2, "None")
default B_3=Armor("Бронежилет 3 класса", 3, 1, 5, 1.5, "None")
default B_4=Armor("Бронежилет 4 класса", 4, 1, 5, 2, "None")