class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Answer(object):
    def __init__(self, Dip, Sum):
        self.dip = Dip
        self.sum = Sum

def insert(v, x):
    if v is None:
        return Node(x)
    if x < v.key:
        v.left = insert(v.left, x)
    elif x > v.key:
        v.right = insert(v.right, x)
    return v

def max_length(v):
    if v is None:
        return Answer(1, 0)
    ans1 = max_length(v.left)
    ans2 = max_length(v.right)
    if (ans1.dip > ans2.dip):
        ans1.dip += 1
        ans1.sum += v.key
        return ans1
    else:
        ans2.dip += 1
        ans2.sum += v.key
        return ans2

root = Node(0)

print("Введи числа")
number = 1
while number:
    try:
        number = int(input())
        root = insert(root, number)
    except:
        print("некорректный ввод")

ans = max_length(root)
print("Длинна самой длинной ветки равна:")
print(ans.dip - 2)
print("Сумма вершин самой длинной ветки равна:")
print(ans.sum)


wait = input()
