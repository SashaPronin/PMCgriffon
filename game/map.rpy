define P1 = False
define P2 = False
# сам экран с картой
screen map:
    modal True
    zorder 100   
# элемент с фоном карты
    fixed:
        xsize 1920 ysize 1080
        add "images/map_g0.png" align (0.8, 0.45)

    fixed:
        xsize 1920 ysize 1080
# иконка 1
        button:
            xpos 1250 ypos 380
            xsize 143 ysize 143
            idle_background "images/map_n1.png"
            hover_foreground "images/map_n1a.png"
            focus_mask True
            tooltip "{b}ул. Кермчин{/b}{p}{i}{size=14}Находится под контролем военной группировки Альтейн.{p} Состав:{p} 56 человек, 2 танка,{p} 3 бмп, 5 техничек{/size}{/i}"
            action Hide("map"), Jump("m1")
            hovered SetScreenVariable("P1", True)
            unhovered SetScreenVariable("P1", False)
        button:
            xpos 700 ypos 580
            xsize 143 ysize 143
            idle_background "images/map_n1.png"
            hover_foreground "images/map_n1a.png"
            focus_mask True
            tooltip "{b}ул. Анита{/b}{p}{i}{size=14}Находится под контролем военной группировки Альтейн.{p} Состав:{p} 56 человек, 2 танка,{p} 3 бмп, 5 техничек{/size}{/i}"
            action Hide("map"), Jump("m2")
            hovered SetScreenVariable("P2", True)
            unhovered SetScreenVariable("P2", False)

    $ tooltip = GetTooltip()

    if P1:
        fixed:
            xpos 1400 ypos 400
            xsize 320 ysize 172
            add "images/map_t2.png"
            text "[tooltip]" xsize 250 ysize 160 align (0.5, 0.5) text_align 0.5
    if P2:
        fixed:
            xpos 850 ypos 600
            xsize 320 ysize 172
            add "images/map_t2.png"
            text "[tooltip]" xsize 250 ysize 160 align (0.5, 0.5) text_align 0.5
