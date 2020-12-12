from typing import List, Tuple

Vector = Tuple[str,int]
Position = Tuple[int, int, str] #X, Y, Facing
Waypoint = Tuple[int,int]

backwardsMapping = { 'N':'S', 'S':'N', 'E':'W', 'W':'E' }
leftMapping = { 'N':'W', 'W':'S','S':'E','E':'N'}
rightMapping = { 'N':'E','E':'S','S':'W','W':'N' }

directionMultiplier = { 'N': (0,-1), 'S': (0,1), 'W': (-1,0), 'E': (1,0) }
    

def load_instructions(filename: str) -> List[Vector]:
    with open(filename) as f:
        lines = [ (line.strip()[0],int(line.strip()[1:])) for line in f.readlines()]    
    
    
    return lines

def apply_instruction(vector: Vector, pos: Position) -> Position:
    (x , y, dir) = pos
    (inst, amt) = vector
    
    if inst in ['F','B']:
        inst = dir if inst =='F' else backwardsMapping[dir]

    
    if inst in ['R','L']:
        while amt > 0:
            dir = rightMapping[dir] if inst=='R' else leftMapping[dir]
            amt-=90

    if inst in ['N','S','E','W']:
        x+=(amt*directionMultiplier[inst][0])
        y+=(amt*directionMultiplier[inst][1])
    

    return (x, y, dir)


def run_part1(filename: str) -> int:
    pos = (0,0,'E')
    instructions = load_instructions(filename)
    for instruction in instructions:
        pos = apply_instruction(instruction, pos)

    print(pos)

    return abs(pos[0]) + abs(pos[1])


def move_waypoint(waypoint: Waypoint, vector: Vector) -> Waypoint:
    (x,y) = waypoint
    (inst, amt) = vector

    if inst in ['N','S','E','W']:
        x+=(amt*directionMultiplier[inst][0])
        y+=(amt*directionMultiplier[inst][1])

    if inst in ['L','R']:
        while (amt > 0):
            (x,y) = rotate_waypoint(x,y,inst)
            amt-=90

    return (x,y)

def rotate_waypoint(x: int, y: int, inst: str) -> Waypoint:
    sector = get_sector(x,y)

    #Bug handle 0 in the sector
    if sector=='XX':
        return (x,y)

    if inst=='R':
        return rotate_right(x,y,sector)
    
    if inst=='L':
        return rotate_left(x,y,sector)

    return (x,y)

def rotate_right(x:int, y:int, sector:str) -> Waypoint:
    if sector=='NE': #move to SE
        tempx = x
        x = abs(y) #North in negative, se we need to make it positive
        y = tempx
    if sector=='SE': #move to SW
        tempx = x
        x = y*-1 #West is negative
        y = tempx
    if sector=='SW': #move to NW
        tempx = x
        x = y*-1 #West is negative
        y = tempx
    if sector=='NW': #move to NE
        tempx = x
        x = abs(y) #East is positive
        y= tempx

    if sector=='N': #if north, right is east
        tempx = x
        x = abs(y)
        y = tempx
    if sector=='E': #if east, right is south
        tempx = x
        x = y
        y = tempx
    if sector=='S': #if south, right is west
        tempx = x
        x = y*-1
        y = tempx
    if sector=='W': #if west, right is north
        tempx = x
        x = y
        y = tempx

    return (x,y)

def rotate_left(x:int, y:int, sector:str) -> Waypoint:
    if sector=='NE': #move to NW
        tempx = x
        x = y 
        y = tempx*-1 #East is positive and becomes - for North
    if sector=='SE': #move to NE
        tempx = x
        x = y 
        y = tempx *-1 #East is positive and becomes - for North
    if sector=='SW': #move to SE
        tempx = x
        x = abs(y) 
        y = abs(tempx) #West is negative and becomes + for South
    if sector=='NW': #move to SW
        tempx = x
        x = y
        y= abs(tempx) #West is negative and + for south

    if sector=='N': #if north, left is west
        tempx = x
        x = y
        y = tempx
    if sector=='W': #if west, left is south
        tempx = x
        x = y
        y = abs(tempx)
    if sector=='S': #if south, left is east
        tempx = x
        x = y
        y = tempx
    if sector=='E': #if east, left is north
        tempx = x
        x = y
        y = tempx*-1
    
    

    return (x,y)

def get_sector(x: int, y: int) -> str:
    if x>0:
        return 'SE' if y>0 else 'NE'
    if x<0:
        return 'SW' if y>0 else 'NW'
    if x == 0:
        return 'S' if y>0 else 'N'
    if y == 0:
        return 'E' if x>0 else 'W'


    return "XX"


def apply_waypoint_instruction(pos: Position, waypoint: Waypoint, vector:Vector) -> Position:
    (x , y, dir) = pos
    (inst, amt) = vector
    (movex, movey) = waypoint

    return (x+movex*amt,y+movey*amt, dir)



def run_part2(filename: str) -> int:
    pos = (0,0,'E')
    waypoint = (10,-1)
    instructions = load_instructions(filename)

    for instruction in instructions:
        if instruction[0] in ['L','R','N','S','W','E']:
            waypoint = move_waypoint(waypoint, instruction)
        else: 
            pos = apply_waypoint_instruction(pos, waypoint, instruction)

    print(pos)

    return abs(pos[0]) + abs(pos[1])


#file = 'test.txt'
file = 'input.txt'
print( run_part1(file))
print( run_part2(file))
