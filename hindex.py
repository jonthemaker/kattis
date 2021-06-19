nbrPaper = int(input())
list = []
for i in range(nbrPaper):
    list.append(input())
list.sort(reverse = False)
h = 0
for i in range(nbrPaper):
    if h == list[i]:
        continue
    if (nbrPaper-i) >= int(list[i]):
        h = list[i]
print(h)
