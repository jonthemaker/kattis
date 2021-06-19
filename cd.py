read = input().split()
N = int(read[0])
M = int(read[1])
listN = []
listM = []
for i in range(N):
    listN.append(int(input()))
for i in range(M):
    listM.append(int(input()))
a = 0
b = 0
count = 0
while (a < N) & (b < M):
    print("\t", listN[a], " : ", listM[b])
    if (a == N-1) & (b < M-1):
        print("a is finished")
        if listN[a] == listM[b]:
            print(" equal")
            count+=1
        b+=1#a is finished
    elif (b == M-1) & (a < N-1):
        print("b is finished")
        if listN[a] == listM[b]:
            print(" equal")
            count+=1
        a+=1#b is finished
    elif listN[a] > listM[b]:
        print(">")
        b+=1#nothing finished
    elif listN[a] < listM[b]:
        print("<")
        a+=1#nothing finished
    elif listN[a] == listM[b]:
        print("equal")
        count+=1
        a+=1
        b+=1
    else:
        print("_")
        a+=1
        b+=1
print(count)
