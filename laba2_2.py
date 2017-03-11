import os, sys, math

while 1:
    os.system('cls')
    print("Введите x(дробное)")
    try:
        x = float(input())
    except:
        print("Некорректный ввод")
        continue
    print("Введите n(целое)")
    try:
        n = int(input())
    except:
        print("Некорректный ввод")
        continue
    answer = 0
    for i in range(1, n):
        answer += (-1)**(i + 1) * x**(2 * i - 1) / math.factorial(2 * i - 1)
    print("Answer = ", answer)
    print("Sin = ", math.sin(x))
    print("e = ", abs(answer - math.sin(x)))
    wait = input()
    break


