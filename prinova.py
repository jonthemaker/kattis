nbrBoys = int(input())
boys = input().split()
interval = input().split()
llim = 0#!
ulim = len(boys)-1#!
for i in range(len(boys)):
    if int(boys[i]) < int(interval[0]):
        llim = i
    if int(boys[i]) > int(interval[1]):
        ulim = i
        break
hot = 0
max = 0
girl = 0
for i in range(ulim-llim):
    if max < int(boys[i+llim+1])-int(boys[i+llim]):
        max = int(boys[i+llim+1])-int(boys[i+llim])
        hot = i+llim
        girl = int(boys[hot]) + int(max/2)
        while (girl < int(interval[0])) | (girl+1 > int(interval[1])):#out of interval
            if (girl < int(interval[0])):
                girl+=1
                max-=2#!
            else:
                girl-=1
                max-=2#!
if girl%2==0:
    girl+=1
print(boys[0], boys[llim])
print(boys[len(boys)-1], boys[ulim])
if int(boys[0]) == int(boys[llim]):
    if max < int(boys[llim])-int(interval[0]):
        girl = int(interval[0])+1
if int(boys[len(boys)-1]) == int(boys[ulim]):
    if max < int(interval[1])-int(boys[ulim]):
        girl = int(interval[1])-1
print(girl)
