import sys
def log(value):
    print(value, file=sys.stderr)

n = int(input())
road = []
commands = []
directions = []
line2 = input().split(";")
for i in range(len(line2)):
    if i == 0:
        x = int(line2[i]) - 1
    else:
        commands.append(line2[i])

for i in range(n):
    r, roadpattern = input().split(";")
    for i in range(int(r)):
        road.append(roadpattern)

for c in commands:
    numStr = ""
    
    for i in c:
        if not i.isalpha():
            numStr += i
        else:
            num = int(numStr)
            char = i
    
    for i in range(num):
        directions.append(char)

for i in range(len(road)):
    if (directions[i] == 'S'):
        listRoad = list(road[i])
        listRoad[x] = "#"
        print(''.join(listRoad))
        
    if (directions[i] == 'L'):
        listRoad = list(road[i])
        x = x - 1
        listRoad[x] = "#"
        print(''.join(listRoad))
        
    if (directions[i] == 'R'):
        listRoad = list(road[i])
        x = x + 1
        listRoad[x] = "#"
        print(''.join(listRoad))