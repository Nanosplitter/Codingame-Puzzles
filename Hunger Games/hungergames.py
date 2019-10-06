import sys
import math

class Tribute:
    def __init__(self, name):
        self.name = name
        self.killed = []
        self.killer = "Winner"
        
    def getKilled(self):
        return ", ".join(sorted(self.killed))
        
    def kill(self, kills):
        k = kills.split(", ")
        for i in k:
            self.killed.append(i)
        return k
t = []
tributes = int(input())

for i in range(tributes):
    player_name = input()
    t.append(Tribute(player_name))

turns = int(input())

for i in range(turns):
    info = input().split(" killed ")
    killer = None
    for j in t:
        if j.name == info[0]:
            killer = j
    kills = killer.kill(info[1])
    for k in t:
        if k.name in kills:
            k.killer = killer.name
first = True
for i in sorted(t, key = lambda x: x.name):
    if not first:
        print()
    print("Name:", i.name)
    if len(i.killed) == 0:
        print("Killed:", "None")
    else:
        print("Killed:", i.getKilled())
    print("Killer:", i.killer)
    first = False