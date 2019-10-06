import math
class Defib:
    def __init__(self, num, name, addr, phone, lo, la):
        self.name = name
        self.addr = addr
        self.phone = phone
        self.lo = float(lo)
        self.la = float(la)
        self.dist = 0
    def setDistance(self, d):
        self.dist = d
defibs = []
lon = float(input().replace(",", "."))
lat = float(input().replace(",", "."))
n = int(input())
for i in range(n):
    d = input().split(";")
    defib = Defib(d[0], d[1], d[2], d[3], d[4].replace(",", "."), d[5].replace(",", "."))
    x = (defib.lo - lon) * math.cos((defib.la + lat)/2)
    y = defib.la - lat
    defib.setDistance((math.sqrt((x**2)+(y**2)) * 6371))
    defibs.append(defib)
print(sorted(defibs, key=lambda x: x.dist)[0].name)