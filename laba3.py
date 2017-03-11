import random

suit = ["♠", "♣", "♥", "♦"]
value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "В", "Д", "К", "Т"]

cards = [value[j] + suit[i]  for i in range(4) for j in range(13)]
mydict = {cards[i]:i for i in range(52)}

def check_cards():
    for i in range(51):
        if (abs(mydict[cards[i]] - mydict[cards[i + 1]]) == 1):
            return True
    return False

while check_cards():
    mid = random.randint(1, 50)
    mid1 = random.randint(0, mid)
    mid2 = random.randint(mid + 1, 51)
    numbers = [0, 1, 2, 3]
    random.shuffle(numbers)
    subdeck = []
    subdeck.append(cards[0:mid1])
    subdeck.append(cards[mid1:mid])
    subdeck.append(cards[mid:mid2])
    subdeck.append(cards[mid2:52])
    cards = subdeck[numbers[0]] + subdeck[numbers[1]] + subdeck[numbers[2]] + subdeck[numbers[3]]

print(cards)

wait = input()
