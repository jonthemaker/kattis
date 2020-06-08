while True:
    nCoordinates = int(input())
    if nCoordinates == 0:
        break;
    xy = []
    for i in range(nCoordinates):
        xy.append(input().split())
    area = 0
    j = nCoordinates-1
    for i in range(nCoordinates):
        area += ( (int(xy[j][0]) + int(xy[i][0])) * (int(xy[j][1]) - int(xy[i][1])) )
        j = i
    if area < 0:
        print("CCW",(-area / 2.0))
    else:
        print("CW",(area / 2.0))
