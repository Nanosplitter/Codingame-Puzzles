import sys
import math

def log(v):
    print(v, file=sys.stderr)

class Floor:
    def __init__(self, width):
        self.arr = []
        for i in range(width):
            self.arr.append("S")
    
    
    def getDirOfElev(self, pos):
        try:
            if self.arr.index("E") > pos:
                return "RIGHT"
            elif self.arr.index("E") == pos:
                return "ON"
            else:
                return "LEFT"
            
        except:
            log("No Elevator with pos: " + str(pos))
    
    def getDirOfExit(self, pos):
        if self.arr.index("X") > pos:
            return "RIGHT"
        else:
            return "LEFT"
    
    def addElevator(self, pos):
        self.arr[pos] = "E"
    
    def addExit(self, pos):
        self.arr[pos] = "X"
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
floors = []
for i in range(nb_floors):
    floors.append(Floor(width))

floors[exit_floor].addExit(exit_pos)
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    floors[elevator_floor].addElevator(elevator_pos)
# game loop
while True:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)
    
    if clone_floor != exit_floor:
        if direction == floors[clone_floor].getDirOfElev(clone_pos):
            print("WAIT")
        elif floors[clone_floor].getDirOfElev(clone_pos) == "ON":
            print("WAIT")
        else:
            print("BLOCK")
    else:
        if direction == floors[clone_floor].getDirOfExit(clone_pos):
            print("WAIT")
        else:
            print("BLOCK")
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # action: WAIT or BLOCK
    