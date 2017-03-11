list1 = []
list2 = []
list3 = []

def merger_list(first_list, second_list):
    mydict = {word:1 for word in first_list}
    mydict.update({word:1 for word in second_list})
    List = []
    for word in mydict:
        List.append(word)
    return List

while 1:
    print("Введите количество строк в 1 списке ")
    try:
        n = int(input())
    except:
        print("Некорректный ввод")
        wait = input()
        continue
    for i in range(n):
        list1.append(input())
    break

while 1:
    print("Введите количество строк во 2 списке ")
    try:
        n = int(input())
    except:
        print("Некорректный ввод")
        wait = input()
        continue
    for i in range(n):
        list2.append(input())
    break

print(merger_list(list1, list2))

wait = input()
