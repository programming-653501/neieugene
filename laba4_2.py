f = open('text.txt', 'r')
mydict = {}

for line in f:
	words = line.split()
	for word in words:
		mydict[word] = 1

for word in mydict:
	print(word)

wait = input()
