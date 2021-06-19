set = 0
while True:
    set+=1
    nbrNames = int(input())
    if nbrNames == 0:
        break
    if (nbrNames%2==0):
        top = ["00"] * (int(nbrNames/2))
        bottom = ["00"] * int(nbrNames/2)
    else:
        top = ["00"] * (int(nbrNames/2) + 1)
        bottom = ["00"] * int(nbrNames/2)
    for i in range(nbrNames):
        if (i%2==0):
            top[int(i/2)] = input()
        else:
            bottom[int(i/2)] = input()
    for i in range(len(bottom)):
        top.append(bottom[len(bottom)-i-1])
    print("SET", set)
    for i in top:
        print(i)
