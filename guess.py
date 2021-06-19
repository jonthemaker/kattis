#1-1000
low = 0
high = 1000
mid = 500
print(mid)
for i in range(9):
    try:
        response = input()
    except EOFError:
        break
    if response == "lower":
        high=mid
        mid=int(mid*0.5)
    elif response == "higher":
        low=mid
        mid=int(mid*1.5)
    else:
        break
    print(mid)
