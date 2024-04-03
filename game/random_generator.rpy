define random_encaunter = False
define current_location_enemy = []
define current_party_enemy = []
define G_number = 0
define number = 1

#random-любая локация с рандомным списком врагов. 
label random:
    $ random_encaunter = False
    $ G_number = 0
    scene 00
    ##задаём список врагов на локации 
    $ location_location_enemy = ['ter1', 'ter2']
    $ current_location_enemy = location_location_enemy
    $ enemy_min = 4
    $ enemy_max = 6
    #
    $ curent_location = 'test1'
    ###
    "[curent_location]"
    "Возможные противники:[current_location_enemy]"
    call random_encaunter
    if random_encaunter == True:
        qwe "rand..."
        $ del current_party_enemy[0:]
        call enemy_generator
        jump Batl_Test
    else:
        qwe "error/r"
        jump start

#-------------------------------------------------
# Random encaunter
label random_encaunter:
    $ random_encaunter = renpy.random.randint(1,1)
    "RE: [random_encaunter]"
    if random_encaunter == 1:
        $ random_encaunter = True
    else:
        $ random_encaunter = False
    return

#-------------------------------------------------
# Generator Enemy
label enemy_generator:
    #Генерируем колличество противников
    $ enemy_number = renpy.random.randint(enemy_min,enemy_max)
    #Получаем список противников
    $ current_location_enemy_number = len(current_location_enemy)
    $ current_location_enemy_number -= 1
    $ current_location_enemy_number = int(current_location_enemy_number)
    $ current_party_enemy = []
    define G_number = 0
    #### "Generator" ####
    $ current_location_enemy_index_number = renpy.random.randint(0, current_location_enemy_number)
    $ enemy_name = current_location_enemy[current_location_enemy_index_number]
    $ enemy1 = enemy_db[enemy_name]
    $ current_party_enemy.append (enemy1['name'])
    if enemy_number>1:
        $ current_location_enemy_index_number = renpy.random.randint(0, current_location_enemy_number)
        $ enemy_name = current_location_enemy[current_location_enemy_index_number]
        $ enemy2 = enemy_db[enemy_name]
        $ current_party_enemy.append (enemy2['name'])
        $ G_number += 1
        if enemy_number>2:
            $ current_location_enemy_index_number = renpy.random.randint(0, current_location_enemy_number)
            $ enemy_name = current_location_enemy[current_location_enemy_index_number]
            $ enemy3 = enemy_db[enemy_name]
            $ current_party_enemy.append (enemy3['name'])
            $ G_number += 1
            if enemy_number>3:
                $ current_location_enemy_index_number = renpy.random.randint(0, current_location_enemy_number)
                $ enemy_name = current_location_enemy[current_location_enemy_index_number]
                $ enemy4 = enemy_db[enemy_name]
                $ current_party_enemy.append (enemy4['name'])
                $ G_number += 1
                if enemy_number>4:
                    $ current_location_enemy_index_number = renpy.random.randint(0, current_location_enemy_number)
                    $ enemy_name = current_location_enemy[current_location_enemy_index_number]
                    $ enemy5 = enemy_db[enemy_name]
                    $ current_party_enemy.append (enemy5['name'])
                    $ G_number += 1
                    if enemy_number>4:
                        $ current_location_enemy_index_number = renpy.random.randint(0, current_location_enemy_number)
                        $ enemy_name = current_location_enemy[current_location_enemy_index_number]
                        $ enemy6 = enemy_db[enemy_name]
                        $ current_party_enemy.append (enemy6['name'])
                        $ G_number += 1
    $ battle_count_enemy = len(current_party_enemy)
    "[battle_count_operator] vz [battle_count_enemy]"
