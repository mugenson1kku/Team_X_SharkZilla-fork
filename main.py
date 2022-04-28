"""
2022 by Team_X_Official & G1tic
Игра простенькая, консольная, и в будушем будут доработки
"""

from random import choice,randint
from colorama import Fore,init
from time import sleep
from lib import *
init(autoreset=True)

""" Cписок название переменных персонажей
ga - Атака Гадзилы
gd - Защита Гадзилы
gx - Ловкость Гадзилы
gHP - Здоровье Гадзилы
sa - Атака Акулы  
sd - Защита Акулы
sx - Ловкость Акулы
sHP - Здоровье Акулы
"""
# Очистка консоли
def clear():
    import os
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')

# Сон 0.5
def s():
    sleep(0.25)

# Сон 2
def s2():
    sleep(2)

# Ретурн
def ret():
    print(f'{r}[!]Вы ввели неверное значение!!!')
    s()
    clear()
    return op()

# Параметры игроков
def op():
    ran = input(f'{lc}Использовать рандом параметры для Гадзиллы?\n{b}[1] - да\n{r}[2] - нет\n{m}>>> ')
    if ran == '1':
        print(f'{b}Хорошо, это я мигом!!!')
        s()
        ga = randint(50, 200)
        gd = randint(1, 49)
        gx = randint(1, 9)
        gHP = randint(50, 500)

        lvl = gx * 50
        points = ga + gd + gHP + lvl
        clear()
                    
        sa = int(points/10)
        sd = int(points/20)
        sx = randint(1, 9)
        sHP = int(points/3)
        f()
        game(ga,gd,gx,gHP,sa,sd,sx,sHP)
    elif ran == '2':
        print(f'{r}Как пожелаете!')
        s()
        clear()
        ga0 = input(f'{r}Введите силу атаки Годзилы(50-200)>>> ')
        ga = int(ga0)
        if ga > 200 or ga < 50:
             ret()
        else:
            s()
            gd0 = input(f'{g}Введите защиту Годзилы(1-49)>>> ')
            gd = int(gd0)
            if gd > 49 or gd < 1:
                ret()
            else:
                s()
                gx0 = input(f'{b}Введите ловкость Годзилы(1-9)>>> ')
                gx = int(gx0)
                if gx > 9 or gx < 0:
                    ret()
                else:
                    lvl = gx * 50
                    gHP0 = input(f'{b}Введите здоровье Годзилы (50-500)>>> ')
                    gHP = int(gHP0)
                    if gHP > 500 or gHP < 50:
                        ret()
                    else:
                        points = ga + gd + gHP + lvl
                        clear()
                    
                        sa = int(points/10)
                        sd = int(points/10)
                        sx = int(gx)
                        sHP = int(points/3)
                        f()
                        game(ga,gd,gx,gHP,sa,sd,sx,sHP)
    else:
        ret()

# Начало боя       
def f():
    print(f'{r}3')
    s()
    print(f'{g}2')
    s()
    print(f'{b}1')
    s()
    clear()
    print(f'{lc}Fight!!!')
    s()
    clear()
    print(f'{y}Fight!!!')
    s()
    clear()
    print(f'{m}Fight!!!')
    s()
    clear()
    print(f'{r}Fight!!!')
    s()
    clear()
    print(f'{g}Fight!!!')
    s()
    clear()
    print(f'{b}Fight!!!')
    clear()

# Код боя
def game(ga,gd,gx,gHP,sa,sd,sx,sHP): 
    s = sleep(0.3)
    s1 = sleep(1)
    a1 = '        '
    a2 = '         '
    a3 = '          '
    pr1 = ''
    pr2 = ''
    pr3 = ''
        
    if ga < 100:
        pr1 = a2
    elif ga < 1000:
        pr1 = a1
    
    if gd < 10:
        pr2 = a3
    elif gd < 100:
        pr2 = a2
    
    if gHP < 100:
        pr3 = a3
    elif gHP < 1000:
        pr3 = a2

        
    set0 = f"""
           {lc}Godzilla VS Shark!

{r}Гадзилла: {ga} ATK{pr1}{r}Акула: {sa} ATK
{m}Гадзилла: {gd} DEF{pr2}{m}Акула: {sd} DEF 
{y}Гадзилла: {gHP} HP{pr3}{y}Акула: {sHP} HP
{b}Гадзилла удача: {gx}0%      {b}Акула удача: {gx}0%
 
"""
    print(set0)
    a = 1 
    
    if ga > sd and sa > gd: 
        for i in range(999): 
            num1 = choice([11 - gx, 0]) 
            num2 = choice([11 - sx, 0]) 
            if a == 1: 
                if gHP > 0 and sHP > 0: 
                    print(f'{b}Гадзилла аттакует!')
                    s
                    print(godz1)
                    s1
                    if num2 > 0: 
                        sHP = sHP - ga + sd
                        print(f'{r}Урон Гадзиллы: {ga - sd}') 
                        s1
                        if sHP < 0:
                            s1
                            print(f'{lc}Здоровье Акулы = 0') 
                        else:
                            print(f'{lc}Здоровье Акулы = {sHP}')
                            s
                            print(f'{b}Акула аттакует!')
                            s
                            print(shark1)
                            s1 
                            if num1 > 0: 
                                gHP = gHP - sa + gd 
                                print(f'{lc}Урон Акулы: {sa - gd}') 
                                s1
                                if gHP < 0:
                                    print(f'{lc}Здоровье Гадзиллы = 0')
                                else:
                                    print(f'{g}Здоровье Гадзиллы = {gHP}')
                                    s1
                            elif num1 == 0:
                                print(f'{y}Гадзилла увернулась!')
                    
                    elif num2 == 0: 
                        print(f'{y}Акула увернулась!') 
                        s1
                        if sHP > 0: 
                            print(f'{lc}Акула аттакует!') 
                            s
                            print(shark1)
                            s2()
                            if num1 > 0: 
                                gHP = gHP - sa + gd 
                                print(f'{lc}Урон акулы: {sa - gd}') 
                                s1
                                if gHP < 0:
                                    print(f'{lc}Здоровье Гадзиллы = 0')
                                else:
                                    print(f'{g}Здоровье Гадзиллы = {gHP}')
                                    s1
                            elif num1 == 0: 
                                print(f'{y}Гадзилла увернулась!') 
                                s1
                else:
                    if sHP <= 0 and a == 1:
                        print(f'{g}Гадзилла победила!') 
                        a = 0
                        s2()
                        back()
                    elif gHP <= 0 and a == 1: 
                        print(f'{g}Акула победила!') 
                        a = 0
                        s2()
                        back()
    else: 
        print(f'{r}[!]Ошибка, защита больше чем атака')
        s2()
        back()

# Инструкция
def inst():
    clear()
    print(f'{y}Инструкция:')
    s()
    print(f'{b}Для того, чтобы начать играть вернитесь в главное меню, и выбирете "Начать игру!"')
    s2()
    print(f'{g}После, у вас будет возможность выбрать ли сами будете выбирать характеристики своего персонажа, или на рандом(на угад).')
    s2()
    print(f'{r}И вы начнете играть!!!')
    s2()
    back()

# Выход 
def ex():
    print(f'{m}Спасибо за использование скрипта!!!\n')
    s2()
    print(f'{r}[!]Завершение работы скрипта через 10 секунд...')
    sleep(9)
    print(f'{lc}Пока!!!')
    sleep(1)
    exit()

# Назад
def back():
    print(f'\n')
    print(f'{y}Вернуться в главное меню?\n{lc}[1] - да\n{g}[2] - нет\n{c}')
    sel = int(input(f'{c}>>> '))
    if sel == 1:
        clear()
        return menu()
    elif sel == 2:
        ex()
    else:
        ret2()

# Главное меню
def menu():
    print(banner)
    print(f'{r}Главное меню\n{lc}[1]Начать игру!\n{b}[2]Инструкция\n{g}[3]Dev`s\n{y}[4]Выход')
    sel = int(input(f'{m}>>> '))
    if sel == 1:
        clear() 
        op()
    elif sel == 2:
        clear()
        inst()
    elif sel == 3:
        clear()
        print(f"""{lc}
TG #1 разработчика: @G1tic
TG #2 разработчика: @Team_X_Official
TG-канал #1 разработчика: @git_zilla 
TG-канал #2 разработчика: @TeamXofficial0
""")
        sleep(2)
        back()
    elif sel == 4:
        ex()
    else:
        ret2()

# Если этот файл будет использоваться как модуль, то банер выводится не будет, а также не будет работать ввод, вывод и т.д.
if __name__ == "__main__": 
    clear() 
    menu()

