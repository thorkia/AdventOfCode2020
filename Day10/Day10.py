
with open('input.txt') as f:
    lines = f.readlines()

adapters = [int(l) for l in lines]

adapters.append(0) #this is the charging outlet

adapters.sort()
index = 0
#Part 1:  Find all the 1 and 3 point differences
onepoint=0
twopoint=0
threepoint = 1 #start at one as my adapter is 3 point?!?
while index+1 < len(adapters):
    diff = adapters[index+1] - adapters[index]
    if diff == 1:
        onepoint+=1    
    if diff == 2:
        twopoint+=1
    elif diff == 3:
        threepoint+=1

    index+=1

print(adapters)
print(onepoint,twopoint,threepoint,onepoint*threepoint, sep=',')

possible_matches = dict()
#add device:
adapters.append(adapters[-1] + 3)

for adapter in adapters:
    possneighbour = [adapter+1,adapter+2,adapter+3]
    neighbours = [ n for n in possneighbour if n in adapters]
    possible_matches[adapter] = neighbours

#count paths to a device
paths = dict()
paths[0] = 1 #there is one path to the socket and starts the count add 0

for adapter, neighbors in possible_matches.items():
    for neighbor in neighbors:
        if neighbor in paths:
            paths[neighbor] += paths[adapter]
        else:
            paths[neighbor] = paths[adapter]
    
print(paths[adapters[-1]])