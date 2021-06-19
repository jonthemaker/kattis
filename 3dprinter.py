wantedStatues = int(input())
printers = 1
day = 1
while printers < wantedStatues:
    printers *= 2
    day += 1
print(day)
