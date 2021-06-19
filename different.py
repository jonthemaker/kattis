nbrs = []
while True:
    try:
        line = input()
    except EOFError:
        break
    nbrs = line.split()
    print(abs(int(nbrs[0])-int(nbrs[1])))
