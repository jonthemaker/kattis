def main():
    Nt = input().split()
    sA = input().split()
    A = []
    N = int(Nt[0])
    t = int(Nt[1])
    for i in sA:
        A.append(int(i))
    Asort = A.copy()
    Asort.sort();
    print(action(N,t,Asort))
    # if (t == 1):
    #     print(t1(N, Asort))
    # elif (t == 2):
    #     print(t2(N, Asort))
    # elif (t == 3):
    #     print(t3(N, Asort))
    # elif (t == 4):
    #     print(t4(N, Asort))
    # elif (t == 5):
    #     print(t5(N, Asort))
def action(N,t,A):
    return [t1,t2,t3,t4,t5][t-1](N,A)


def t1(N, A):
    for i in range(N):
        if ((A[N-1-i] + A[N-2-i]) == 7777):
            return ("Yes")
        if A[N-1-i] < (7777/2):
            return ("No")

    return ("No")
def t2(N, A):
    for i in range(N-1):
        if (A[i] == A[i+1]):
            return ("Contains duplicate")
    return ("Unique")
def t3(N, A):
    hash = [0]*(A[N-1]+1)
    for i in range(N):
        hash[A[i]]+=1
    maxi = max(hash)
    if maxi > N/2:
        return (hash.index(maxi))
    else:
        return (-1)
def t4(N, A):
    if N % 2 == 0:
        return str(A[N//2-1]) + " " + str(A[N//2])
    else:
        return str(A[N//2])
def t5(N, A):
    string = ""
    for i in A:
        if (i > 99) & (i < 1000):
            string += str(i) + " "
    return (string[0:len(string)-1])

main()
