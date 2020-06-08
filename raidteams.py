nbrPlayers = int(input())
players = []
teams = []
team = []
count = 0

def kq(v):
    value = ""
    for c in v:
        if c.isdigit():
            value = value + c
    return int(value)

for i in range(nbrPlayers):
    players.append(input().split())
while (len(players)+len(team))/3 >= 1:
    best = max(players,key=lambda x:x[count+1])
    team.append(best)
    players.remove(best)

    if count == 2:
        team.sort(key=lambda x:kq(x[0]))
        teams.append(team)
        team = []
    count = (count+1)%3
for i in teams:
    print(i)
