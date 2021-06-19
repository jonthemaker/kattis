strings = []
strings = input().split()

def consist(strs):
    for i in range(len(strs)):
        for j in range(len(strs)-i-1):
            if (strs[i] == strs[j+i+1]):
                return str("no")
    return str("yes")

print(consist(strings))
