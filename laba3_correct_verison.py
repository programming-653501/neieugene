import os, sys

def cls():
    os.system('cls')

def write_playing_field():
    print("   ", end = "")
    for i in range(1, length + 1):
        print(i, " ", end = "")
    print()
    for i in range(length):
        print(i + 1, playing_field[i])    

length, width = 0, 0

while 1:   # Ввод длины
    print("Введите длину пирога (0 < n < 10)")
    try:
        length = int(input())
        if (length < 0):
            cls()
            print("Длина не может быть отрицательной!!!")
            continue
        if (length == 0):
            cls()
            print("Длина не может быть нулевой!!!")
            continue
        if (length > 9):
            cls()
            print("Слишком большая длина!!!")
            continue
    except:
        print("Некорректный ввод!!!")
        continue
    break

while 1: # Ввод ширины
    print("Введите ширину пирога (0 < m < 10)")
    try:
        width = int(input())
        if (width < 0):
            cls()
            print("Ширина не может быть отрицательной!!!")
            continue
        if (width == 0):
            cls()
            print("Ширина не может быть нулевой!!!")
            continue
        if (width > 9):
            cls()
            print("Слишком большая ширина!!!")
            continue
    except:    
        print("Некорректный ввод!!!")
        continue
    break

playing_field = [0] * length # заполняем массив 0
for i in range(length):
    playing_field[i] = [0] * width

playing_field[length - 1][0] = 1 # левая нижняя клетка отравлена

cls() # отчистить консоль
write_playing_field()

while 1:
    marker1 = True
    marker2 = True
    while marker1  and playing_field[length - 1][0] == 1:
        print("Ходит 1 игрок")
        print("Введи координаты клетки (x, y - натуральные числа)")
        print("Введи x")
        try:
            x = int(input())
            if (x < 1 or x > length):
                cls()
                write_playing_field()
                print("x должно быть в пределах поля")
                continue
        except:
            cls()
            write_playing_field()
            print("Некорректный ввод")
            continue
        print("Введи y")
        try:
            y = int(input())
            if (y < 1 or y > width):
                cls()
                write_playing_field()
                print("y должно быть в пределах поля")
                continue
        except:
            cls()
            write_playing_field()
            print("Некорректный ввод")
            continue
        if (playing_field[x - 1][y - 1] == 1):
            playing_field[x - 1][y - 1] = -1
            print("Вы съели отравленый кусок, победил второй игрок")
            playing_field[length - 1][0] == 100
            break
        elif (playing_field[x - 1][y - 1] != 0):
            cls()
            write_playing_field()
            print("На этой клетке нет пирога, введите клетку на которой есть пирог")
            continue
        else:
            for i in range(0, x):
                for j in range(y - 1, width):
                    playing_field[i][j] = -1
            cls()
            write_playing_field()
            print("Вы съели кусок пирога")
            marker1 = False
    while marker2 and playing_field[length - 1][0] == 1:
        print("Ходит 2 игрок")
        print("Введи координаты клетки (x, y - натуральные числа)")
        print("Введи x")
        try:
            x = int(input())
            if (x < 1 or x > length):
                cls()
                write_playing_field()
                print("x должно быть в пределах поля")
                continue
        except:
            cls()
            write_playing_field()
            print("Некорректный ввод")
            continue
        print("Введи y")
        try:
            y = int(input())
            if (y < 1 or y > width):
                cls()
                write_playing_field()
                print("y должно быть в пределах поля")
                continue
        except:
            cls()
            write_playing_field()
            print("Некорректный ввод")
            continue
        if (playing_field[x - 1][y - 1] == 1):
            playing_field[x - 1][y - 1] = -1
            print("Вы съели отравленый кусок, победил первый игрок")
            playing_field[length - 1][0] == 100
            break
        elif (playing_field[x - 1][y - 1] != 0):
            cls()
            write_playing_field()
            print("На этой клетке нет пирога, введите клетку на которой есть пирог")
            continue
        else:
            for i in range(0, x):
                for j in range(y - 1, width):
                    playing_field[i][j] = -1
            cls()
            write_playing_field()
            print("Вы съели кусок пирога")
            marker2 = False
    
wait = input()
