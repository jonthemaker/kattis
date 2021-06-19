global hash

def isPrime(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if n % i == 0:
                return 0
        return 1
    return 1
def sieve(n):
    v0 = 0
    for i in range(2, n+1):
        if isPrime(i) == 1:
            hash[i] = 1
            v0+=1
    return v0

n,q = input().split()
n,q = int(n), int(q)
hash = [None] * (n+1)
hash[1] = 0
nPrimes = sieve(int(n))
queries = []
for i in range(q):
    queries.append(int(input()))

#for kattis
print(nPrimes)
for i in queries:
    print(hash[i])
