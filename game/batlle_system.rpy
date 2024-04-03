init python:
    # Объявляем изображения игрока и врага
    image player_image = "player.png"
    image enemy_image = "enemy.png"
    
    # Здоровье игрока и врага
    player_hp = 100
    enemy_hp = 100
    enemy_damage = 20  # Урон, наносимый врагом

    while player_hp >0:

        # Ход игрока

        menu:
            "Attack":
                $ enemy_hp -= 10
                "Это сильный удар! У врага [enemy_hp] хп!"
                if enemy_hp <= 0:
                    "Вы выиграли боевое столкновение!"
                    jump simple_end
            "Defend":
                $ player_hp -= enemy_damage // 2
                "Вы защищаетесь и уменьшаете урон до [player_hp]!"

        # Ход противника
        $ player_hp -= enemy_damage
        "Враг атакует, уменьшая ваше здоровье до [player_hp]!"

    "Вы умерли..."
    screen hp_bars_1v1:

    vbox:
        spacing 20
        xalign 0.1
        yalign 0.0
        xmaximum 600
        text "Player 1"
        bar value player_hp range player_max_hp
    vbox:
        spacing 20
        xalign 0.9
        yalign 0.0
        xmaximum 600
        text "enemy"
        bar value enemy_hp range enemy_max_hp

    # Ход игрока – два варианта!
    call dice_roll

        menu:
            "Легкая атака":
                call camera_knight_attack
                if d10 >= 8:                                                # 30%
                    $ player_attack_value = d4 + d6
                    $ enemy_hp -= player_attack_value
                    "Критический удар! [player_attack_value] урон!"          # 70%
                else:
                    $ enemy_hp -= d4
                    "[d4] повреждён!"
            "Сильная атака":
                call camera_knight_attack                       
                if d10 >= 9:                                                # 20%
                    $ player_attack_value = (d6 + d4)*2
                    $ enemy_hp -= player_attack_value
                    "Критический удар! Вы нанесли  [player_attack_value] урон!"
                elif d10 >= 5:                                              # 40%  
                    $ player_attack_value =  d6 + 2                                        
                    $ enemy_hp -= player_attack_value
                    "Это сильный удар! Враг забирает [player_attack_value] хп!"
                else:                                                       # 40% 
                    "ты скучаешь!"
                if enemy_hp <= 0:
                    call camera_knight_win
                    "Вы выиграли боевое столкновение!"
                    jump harder_menu

                     # Enemy Turn - Semi-randomized behavior!

                call dice_roll

                if d20 >= 19:                                            # 20%       
                    call camera_skeleton_attack                                                                                
                    $ player_hp -= d10
                    "Враг совершает дикую атаку, нанося [d10] урона!"
                elif d20 <=2:                                            # 20%
                    $ enemy_hp += d4
                    if enemy_hp < enemy_max_hp:
                        "Враг лечит себя, поднимая [d4] здоровья!"
                else:
                    $ enemy_hp = enemy_max_hp
                    "Враг полностью восстанавливает свое здоровье!"
            else:                                                    # 60%
                call camera_skeleton_attack                                                                                
                $ player_hp -= d4
                "Враг атакует, нанося [d4] урона!"

    
    # Генератор случайных чисел
    label dice_roll:
        $ d4 = renpy.random.randint(1, 4)
        $ d6 = renpy.random.randint(1, 6)
        $ d10 = renpy.random.randint(1, 10)
        $ d20 = renpy.random.randint(1, 20)
        return

    label start:

        hide black


