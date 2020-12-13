from typing import List, Tuple



def load_instructions(filename: str) -> Tuple[int,List[str]]:
    with open(filename) as f:
        time = f.readline().strip()
        buses = f.readline().strip().split(',')
    
    return (int(time), buses)


def run_part1(filename: str):
    (arrivaltime, buses) = load_instructions(filename)
    
    busid = -1
    waittime = -1
    
    for bus in buses:
        if bus.isnumeric() == False:
            continue

        bus = int(bus)
        remainder = arrivaltime % bus
        remainDiff = bus-remainder
        if waittime == -1 or remainDiff < waittime:
            busid = bus
            waittime = remainDiff

    print("Arrival Time ", arrivaltime)
    print("Bus Id ", busid)
    print("Minutes Wait ", waittime)

    print(waittime*busid)

 
def all_diff_equalindex(timestamp:int, buses:List[Tuple[int,int]]) -> bool:
    #check if the first bus is at 0 minute wait
    if timestamp % int(buses[0][0]) != 0:
        return False;

    index = 0
    while index+1 < len(buses):        
        index+=1
        
        busid = int(buses[index][0])
        minutewait = busid - (timestamp % busid) #calculate the minutes to wait until it departs
        if minutewait != buses[index][1]: #if the minute wait is not equal to the index, then we don't have the correct positions
            return False
        
    
    return True


def run_part2(filename: str):
    (arrivaltime, buses) = load_instructions(filename)    
    timestamp = -int(buses[0])
    allmet = False

    realbuses = [ (int(b),buses.index(b)) for b in buses if b.isnumeric()]
    increment = max( [int(b) for b in buses if b.isnumeric()])

    while allmet == False:
        timestamp+=realbuses[0][0] # bus 0 has to arrive at the right time
        allmet = all_diff_equalindex(timestamp,realbuses)
    
    print(timestamp)


filename='test.txt'
#filename='input.txt'

run_part1(filename)
run_part2(filename)