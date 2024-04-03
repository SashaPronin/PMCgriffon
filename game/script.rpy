
label start:
    show screen map
    qwe "123"

label m1:
    scene 00
    qwe "ул. Кермчин"
    jump start
    return

label m2:
    scene 00
    qwe "ул. Кермчин"
    M200 "Замечен противник..."
    menu:
        M200 "Что делать?..."
        "Вступить в бой":
            jump test1
        "ждать":
            jump test2
label test1:
    scene 00
    qwe "бой"
    jump random

label test2:
    scene 00
    qwe "Ничего не происходит..."
    menu:
        M200 "Что делать?..."
        "Вступить в бой":
            jump test1
        "ждать":
            jump test2
        "отступить":
            jump start