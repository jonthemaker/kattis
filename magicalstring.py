nbrInputs = int(input())
ascii = [0]*128 #all ascii
asciilist = [] #ascii used in ascii
magical = []

for i in range(nbrInputs):
    magical.append(input().split())
    print("",magical[i][1])
    for j in range(int(magical[i][1])):#K
        print("\t",magical[i][0])
        points = []
        points.append(0)
        theletter = ""
        for k in range((len(magical[i][0])-4)):#figures out what character is best to place
            substring = magical[i][0][k:k+5]
            print("\t\t",substring)
            a = list(substring)
            for l in a:
                if ascii[ord(l)] == 0:
                    asciilist.append(ord(l))
                ascii[ord(l)] += 1
            for l in asciilist:#process points
                if ascii[l] > points[len(points)-1]:
                    points[len(points)-1] = ascii[l]
                    theletter = l
            ascii = [0]*128
            asciilist = []
        print("\t\t",points," = ",theletter)#got the character to place
        
        # chararray = list(magical[i][0])
        # chararray[1] = theletter
        # string = ""
        # for k in range(len(chararray)):
        #     string += chr(chararray[k])
        # magical[i][0] = string
print(ascii)
