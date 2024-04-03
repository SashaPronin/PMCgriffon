# просто персонаж для теста
define qwe = Character('M-15')
#Оперативники в игре:
define M4 = Character('M-4', calor="#db6fc4")
define U45 = Character('M-15', calor="#e6b822")
define M200 = Character('M200', calor="#4d4d4d")
#------------------------------------------------
#Характеристики:
#================================================
label chard_db:
    define chard_db = {
        'M4':
            {
                'name': 'M-4', #Имя персонажа
                'max_heat': 100, #Максимальное здоровье персонажа
                'time_heat': 100, #Текущие здоровье персонажа
                'min_heat': 0,#Минимально допустимое
                'pawer': 5,#Сила (для носки оружия и т.д.)
                'damage': 40,#урон в ближнем
                'class': 'hedgehopper',#класс, чего не понятно?
                'def_0': 3,#защита ближняя
                'def_1': 5,#защита дальняя
                'speed': 6,#скорость
                'time_exp': 0,#текущий опыт
                'app_exp': 100,#опыт, для левл апа
                'level': 1,#уровень
                'c_armor':'',#броня
                'c_helmet':'',#шлем
                'c_wepon':'',#оружие
                'image': ""#картинка персонажа. (что-бы вывести его на поле битвы)
            },
        'U45':
            {
                'name': 'M-15', #Имя персонажа
                'max_heat': 185, #Максимальное здоровье персонажа
                'time_heat': 185, #Текущие здоровье персонажа
                'min_heat': 0,#Минимально допустимое
                'pawer': 5,#Сила (для носки оружия и т.д.)
                'damage': 40,#урон в ближнем
                'class': 'hedgehopper',#класс, чего не понятно?
                'def_0': 5,#защита ближняя
                'def_1': 4,#защита дальняя
                'speed': 8,#скорость
                'time_exp': 0,#текущий опыт
                'app_exp': 100,#опыт, для левл апа
                'level': 1,#уровень
                'c_armor':'',#броня
                'c_helmet':'',#шлем
                'c_wepon':'',#оружие
                'image': ""#картинка персонажа. (что-бы вывести его на поле битвы)
            },
        'U09':
            {
                'name': 'M-15', #Имя персонажа
                'max_heat': 176, #Максимальное здоровье персонажа
                'time_heat': 176, #Текущие здоровье персонажа
                'min_heat': 0,#Минимально допустимое
                'pawer': 4,#Сила (для носки оружия и т.д.)
                'damage': 40,#урон в ближнем
                'class': 'hedgehopper',#класс, чего не понятно?
                'def_0': 5,#защита ближняя
                'def_1': 4,#защита дальняя
                'speed': 7,#скорость
                'time_exp': 0,#текущий опыт
                'app_exp': 100,#опыт, для левл апа
                'level': 1,#уровень
                'c_armor':'',#броня
                'c_helmet':'',#шлем
                'c_wepon':'',#оружие
                'image': ""#картинка персонажа. (что-бы вывести его на поле битвы)
            },
        'M200':
            {
                'name': 'M-15', #Имя персонажа
                'max_heat': 88, #Максимальное здоровье персонажа
                'time_heat': 88, #Текущие здоровье персонажа
                'min_heat': 0,#Минимально допустимое
                'pawer': 5,#Сила (для носки оружия и т.д.)
                'damage': 20,#урон
                'class': 'sniper',#класс, чего не понятно?
                'def_0': 1,#защита ближняя
                'def_1': 3,#защита дальняя
                'speed': 3,#скорость
                'time_exp': 0,#текущий опыт
                'app_exp': 100,#опыт, для левл апа
                'level': 1,#уровень
                'c_armor':'',#броня
                'c_helmet':'',#шлем
                'c_wepon':'',#оружие
                'image': ""#картинка персонажа. (что-бы вывести его на поле битвы)
            }
        }

    define current_count_operator = ['M4']
    define battle_count_operator = 0
    $ battle_count_operator = len(current_party_operator)