"""
2022 by Team_X_Official, G1tic & mugenson1kku
Игра простенькая, консольная, и в будушем будут доработки
"""

from random import choice,randint
from colorama import Fore,init
from time import sleep
from lib import *
init(autoreset=True)

""" Cписок переменных у персонажей:
ga - Атака Годзиллы
gd - Защита Годзиллы
gx - Ловкость Годзиллы
gHP - Здоровье Годзиллы
sa - Атака Акулы  
sd - Защита Акулы
sx - Ловкость Акулы
sHP - Здоровье Акулы
lvl - Я хз что это, но высчитывается значение как-то странно
points - см. lvl
"""
# Очистка консоли
def clear():
    import os
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    else:
        os.system('clear')

# Ретурн
def ret():
    print(f'{r}[!]Вы ввели неверное значение!')
    sleep(0.25)
    clear()
    return op()

# Параметры игроков
def op():
    ran = input(f'{lc}Использовать рандом параметры для Годзиллы?\n{b}[1] - да\n{r}[2] - нет\n{m}>>> ')
    if ran == '1':
        print(f'{b}Хорошо, это я мигом!')
        sleep(0.25)
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
        sleep(0.25)
        clear()
        ga0 = input(f'{r}Введите силу атаки Годзиллы(50-200)>>> ')
        ga = int(ga0)
        if ga > 200 or ga < 50:
             ret()
        else:
            sleep(0.25)
            gd0 = input(f'{g}Введите защиту Годзиллы(1-49)>>> ')
            gd = int(gd0)
            if gd > 49 or gd < 1:
                ret()
            else:
                sleep(0.25)
                gx0 = input(f'{b}Введите ловкость Годзиллы(1-9)>>> ')
                gx = int(gx0)
                if gx > 9 or gx < 0:
                    ret()
                else:
                    lvl = gx * 50
                    gHP0 = input(f'{b}Введите здоровье Годзиллы (50-500)>>> ')
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
    sleep(0.25)
    print(f'{g}2')
    sleep(0.25)
    print(f'{b}1')
    sleep(0.25)
    clear()
    print(f'{lc}Fight!!!')
    sleep(0.25)
    clear()
    print(f'{y}Fight!!!')
    sleep(0.25)
    clear()
    print(f'{m}Fight!!!')
    sleep(0.25)
    clear()
    print(f'{r}Fight!!!')
    sleep(0.25)
    clear()
    print(f'{g}Fight!!!')
    sleep(0.25)
    clear()
    print(f'{b}Fight!!!')
    clear()

# Код боя
def game(ga,gd,gx,gHP,sa,sd,sx,sHP): 
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

{r}Годзилла: {ga} ATK{pr1}{r}Акула: {sa} ATK
{m}Годзилла: {gd} DEF{pr2}{m}Акула: {sd} DEF 
{y}Годзилла: {gHP} HP{pr3}{y}Акула: {sHP} HP
{b}Годзилла: {gx}0% LUCK      {b}Акула: {gx}0% LUCK
 
"""
    print(set0)
    #TODO: заменить set0 на это
#    print("Годзилла против Акулы!\n"
#          "\n"
#          "Годзилла: {ga} ATK{pr1} Акула: {sa} ATK"
#          "Годзилла: {gd} DEF{pr2} Акула: {sd} DEF"
#          "Годзилла: {gHP} HP{pr3} Акула: {sHP} HP"
#          "Годзилла: {gx}0% LUCK   Акула: {gx}0% LUCK")
    a = 1 
    
    if ga > sd and sa > gd: 
        for i in range(999): 
            num1 = choice([11 - gx, 0]) 
            num2 = choice([11 - sx, 0]) 
            if a == 1: 
                if gHP > 0 and sHP > 0: 
                    print(f'{b}Гадзилла аттакует!')
                    sleep(0.3)
                    print(godz1)
                    sleep(1)
                    if num2 > 0: 
                        sHP = sHP - ga + sd
                        print(f'{r}Урон Гадзиллы: {ga - sd}') 
                        sleep(1)
                        if sHP < 0:
                            sleep(1)
                            print(f'{lc}Здоровье Акулы = 0') 
                        else:
                            print(f'{lc}Здоровье Акулы = {sHP}')
                            sleep(0.3)
                            print(f'{b}Акула аттакует!')
                            sleep(0.3)
                            print(shark1)
                            sleep(1) 
                            if num1 > 0: 
                                gHP = gHP - sa + gd 
                                print(f'{lc}Урон Акулы: {sa - gd}') 
                                sleep(1)
                                if gHP < 0:
                                    print(f'{lc}Здоровье Гадзиллы = 0')
                                else:
                                    print(f'{g}Здоровье Гадзиллы = {gHP}')
                                    sleep(1)
                            elif num1 == 0:
                                print(f'{y}Гадзилла увернулась!')
                    
                    elif num2 == 0: 
                        print(f'{y}Акула увернулась!') 
                        sleep(1)
                        if sHP > 0: 
                            print(f'{lc}Акула аттакует!') 
                            sleep(1)
                            print(shark1)
                            sleep(2.0)
                            if num1 > 0: 
                                gHP = gHP - sa + gd 
                                print(f'{lc}Урон акулы: {sa - gd}') 
                                sleep(1)
                                if gHP < 0:
                                    print(f'{lc}Здоровье Гадзиллы = 0')
                                else:
                                    print(f'{g}Здоровье Гадзиллы = {gHP}')
                                    sleep(1)
                            elif num1 == 0: 
                                print(f'{y}Гадзилла увернулась!') 
                                ssleep(1)
                else:
                    if sHP <= 0 and a == 1:
                        print(f'{g}Гадзилла победила!') 
                        a = 0
                        sleep(2.0)
                        back()
                    elif gHP <= 0 and a == 1: 
                        print(f'{g}Акула победила!') 
                        a = 0
                        sleep(2.0)
                        back()
    else: 
        print(f'{r}[!]Ошибка, защита больше чем атака')
        sleep(2.0)
        back()

# Инструкция
def inst():
    clear()
    print(f'{y}Инструкция:')
    print(f'{b}Для того, чтобы начать играть вернитесь в главное меню, и выбирете "Начать игру!"')
    print(f'{g}После, у вас будет возможность выбрать ли сами будете выбирать характеристики своего персонажа, или на рандом(на угад).')
    print(f'{r}И вы начнете играть!!!')
    back()

# Выход 
def ex():
    print(f'{m}Спасибо за использование скрипта!!!\n')
    sleep(2.0)
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

