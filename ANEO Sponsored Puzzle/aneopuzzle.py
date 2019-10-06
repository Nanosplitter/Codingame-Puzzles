import math
mpsConvert = 1000/3600
class Light:
    def __init__(self, dist, dur):
        self.dist = dist
        self.dur = dur

def goForGreen(speed, Light):
    timeToLight = roundUpToNearest(Light.dist / (speed*mpsConvert), Light.dur)
    if(timeToLight%Light.dur==0 and timeToLight%(Light.dur*2)!=0):
        return True
    else:
        return False
        
def roundUpToNearest(x, base):
    if (round(x, 9)%base==0):
        return int(base * math.ceil(float(x+base)/base))
    return int(base * math.ceil(float(x)/base))

s = int(input())
lights = []
works = True
light_count = int(input())
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    lights.append(Light(distance, duration))
    
for i in range(1, s+1)[::-1]:
    works = True
    for l in lights:
        if not goForGreen(i, l):
            works = False
    if works:
        print(i)
        quit()