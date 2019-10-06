import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x, y = [int(i) for i in input().split()]

bottomLimit = h
topLimit = 0
rightLimit = w
leftLimit = 0
# game loop

def log(v,v2):
    print(str(v) + ":", v2, file=sys.stderr)

while True:
    b = input() # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    distFromRight = abs(rightLimit - x)
    distFromLeft = abs(leftLimit - x)
    distFromTop = abs(topLimit - y)
    distFromBottom = abs(bottomLimit - y)


    if b[0] == "D":
        topLimit = y
        y += math.ceil(distFromBottom / 2)
        log("Y-diff", math.ceil(distFromBottom / 2))
    elif b[0] == "U":
        bottomLimit = y
        y -= math.ceil(distFromTop / 2)
        log("Y-diff", math.ceil(distFromTop / 2))
    elif b[0] == "R":
        leftLimit = x
        x += math.ceil(distFromRight / 2)
        log("X-diff", math.ceil(distFromRight / 2))
    else:
        rightLimit = x
        x -= math.ceil(distFromLeft / 2)
        log("X-diff", math.ceil(distFromLeft / 2))
    
    if len(b) == 2:
        if b[1] == "R":
            leftLimit = x
            x += math.ceil(distFromRight / 2)
            log("X-diff", math.ceil(distFromRight / 2))
        else:
            rightLimit = x
            x -= math.ceil(distFromLeft / 2)
            log("X-diff", math.ceil(distFromLeft / 2))
    log("distFromRight", distFromRight)
    log("distFromLeft", distFromLeft)
    log("distFromTop", distFromTop)
    log("distFromBottom", distFromBottom)
    log("topLimit", topLimit)
    log("bottomLimit", bottomLimit)
    log("rightLimit", rightLimit)
    log("leftLimit", leftLimit)
    print(x, y)