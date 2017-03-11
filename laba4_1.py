border_letters = {}
words = []

while 1:
    print("Введите количество слов")
    try:
        n = int(input())
    except:
        print("Некорректный ввод")
        continue
    for i in range(n):
        s = input()
        words.append(s)
        try:
            border_letters[s[:1]] += 1
        except:
            border_letters[s[:1]] = 1
        try:
            border_letters[s[-1:]] -= 1
        except:
            border_letters[s[-1:]] = -1       
    break

count = 0

for i in border_letters:
    if (border_letters[i]):
        count += 1

if (count > 2):
    print("Невозможно составить цепочку слов")
else:
    for i in range(n):
        for j in range(n):
            if (words[j][:1] == words[i][-1:]):
                words[i + 1], words[j] = words[j], words[i + 1]
    for i in words:
        print(i, end ="")

wait = int(input())

        
