import os,sys

inside_minutes = 0
outside_minutes = 0
gigabyte = 0
marker = False

name_tariffs = ["Комфорт", "Комфорт 2", "Комфорт 4", "Комфорт 8", "Smart бесконечный"]
outside_minutes_tariffs = [100, 200, 300, 400, 1000000000]
gigabyte_tariffs = [1, 2, 4, 8, 1000000000]

def display_menu():
    os.system('cls')
    print("Меню")
    print("1. Ввести данные.")
    print("2. Расчет оптимального тарифа.")
    print("3. Информация о тарифах.")
    print("4. Обратная связь.")
    print("5. Выход.")
    print("Введите число (1 - 5) ")

def tariff_calculation():
    global marker
    if (not marker):
        print("Сначала введите данные")
        wait = input()
        return
    else:
        for i in range(4):
            if (outside_minutes <= outside_minutes_tariffs[i] and gigabyte <= gigabyte_tariffs[i]):
                print("Ваш оптимальный тариф - " + name_tariffs[i])
                wait = input()
                return
    print("Нет оптимального тарифа")
    wait = input()

def data_input():
    global inside_minutes, outside_minutes, gigabyte, marker
    os.system('cls')
    print("Все данные вводяться в среднем в месяц")
    print("Введите количество минут внутри сети: ")
    try:
        inside_minutes = int(input())
        if (inside_minutes < 0):
            print("Число не может быть отрицательным")
            wait = input()
            return
    except:
        data_input()
    print("Введите количество минут на другие сети: ")
    try:
        outside_minutes = int(input())
        if (outside_minutes < 0):
            print("Число не может быть отрицательным")
            wait = input()
            return
    except:
        data_input()
    print("Введите количество гигабайт интернет-трафика: ")
    try:
        gigabyte = int(input())
        if (gigabyte < 0):
            print("Число не может быть отрицательным")
            wait = input()
            return
        marker = True
    except:
        data_input()

def tariff_information():
    for i in range(4):
        print("Тариф - " ,name_tariffs[i],  "Минуты вне сети - " , outside_minutes_tariffs[i], "Гигабайт интернет трафика - ", gigabyte_tariffs[i])
    wait = input()


def feedback():
    os.system('cls')
    print("Связаться с нами: 411 \nЗвонок бесплатный в сети velcom")
    wait = input()

while True:
    display_menu()
    try:
        x = int(input())
    except:
        continue
    if (x < 1 or x > 5):
        continue
    if (x == 1):
        data_input()
    if (x == 2):
        tariff_calculation()
    if (x == 3):
        tariff_information()
    if (x == 4):
        feedback()
    if (x == 5):
        break
