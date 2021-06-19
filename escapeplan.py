class Point:
    def __init__(self, x, y, identifier):
        self.x = float(x)
        self.y = float(y)
        self.identifier = identifier
        self.tempcounter = 0
    def print(self):
        print(identifier,self.x,":",self.y)
    def __repr__(self):
        return self.identifier
class Box:
    def __init__(self, ID, list):
        self.ID = ID
        self.content = list
    def __repr__(self):
        return str(self.ID)

def readlines(nLines, type = "H"):
    list = []
    for i in range(nLines):
        xy = input().split()
        list.append(Point(xy[0],xy[1],type+str(i)))
    return list

def mostUnique(list):#2D arrray/list as parameter
    val = 0
    uniqueBox = list[0]
    for i in list[0].content:
        val += i.tempcounter#combined value for a robot
    for i in list[1:]:
        temp = 0
        for j in i.content:
            temp+=j.tempcounter#combined value for a robot
        if temp < val:
            val = temp
            uniqueBox = i
    return uniqueBox

def lowest(list):#1D array/list as parameter
    if len(list) == 0:
        return 0
    min = list[0]
    for i in list[1:]:
        if i.tempcounter < min.tempcounter:
            min = i
    return min

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

scenario = 0
scenarios = []
while True:
    scenario+=1
    set = int(input())
    if set == 0:
        break
    robots = readlines(set, "R")#lines = m
    holes = readlines(int(input()))#lines = n

    """through smallest between m and n method - by fewest possible connections first"""

    if (len(holes) == 0):#0 holes no robots will remain undamaged
        scenarios.append(Box(scenario, [0,0,0]))
        continue

    time = 2.5
    times = []
    for i in range(3):
        time*=2
        connections = []#double arrray
        id = -1
        for i in robots:
            id+=1
            options = []
            for j in holes:
                import math
                hypo = math.sqrt((i.x - j.x)**2 + (i.y - j.y)**2)
                #print(" hypo",hypo)
                if hypo < (time*10):
                    #print(i.identifier,"<->",j.identifier)#in reach
                    options.append(j)
            connections.append(Box(id, options))

        """available connections"""
        for i in connections:
            for j in i.content:
                j.tempcounter+=1

        """selecting connections"""
        final = [0]*len(connections)
        while len(connections) > 0:
            #finding the most unique connection
            uniqueBox = mostUnique(connections)#unique[0] = 1D list, unique[1] = int
            leastFrequent = lowest(uniqueBox.content)
            final[uniqueBox.ID] = leastFrequent
            #remove least frequent from all connections
            connections.remove(uniqueBox)#robot has found itself a hole to occupy, therby finished and will be removed from the search
            if leastFrequent != 0:
                for i in connections:
                    i.content.remove(leastFrequent)#hole has reached maximum capacity, therby remove hole as option for other robots

        count = 0
        for i in final:
            if i != 0:
                count+=1
        times.append(count)
    scenarios.append(Box(scenario,times))
for i in scenarios:#OUTPUT
    print("Scenario",i.ID)#OUTPUT
    count = 2.5
    for j in i.content:
        count = count*2
        print("In",count,"seconds",j,"robot(s) can escape")

    """
    1    ABC
    2    A
    3    B
    2 3 / 1

    1    ABCE
    2    BC
    3    BC
    4    BE
    2 3 4 / 1

    A   1
    B   123
    C   23
    D
    E   4
    D / A E / C / B


    A   234
    B   123
    C   124
    D   134
    E   23
    """
