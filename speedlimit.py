values = []
round = -1
distance = 0
carry = 0
while True:
    k = input().split()
    if round == 0:
        values.append(distance)
    if len(k) == 1:
        round = int(k[0])
        carry = 0
        distance = 0
    else:
        distance += int(k[0])*(int(k[1])-carry);
        carry = int(k[1])
        round = round - 1
    if k[0] == "-1":
        break;
for i in values:
    print(str(i) + " miles")
