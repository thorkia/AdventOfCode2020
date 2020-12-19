from typing import List, Tuple, Set

Node = Tuple[int,int,int,bool] #,x,y,z,state

def get_input(filename: str) ->List[Node]:
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    nodes = list()
    for y in range(0,len(lines)):
        for x in range(0, len(lines[y])):
            if lines[y][x] == '#':
                nodes.append( (x,y,0,True) )
            else:
                nodes.append( (x,y,0,False) )

    return nodes

def generate_node_name(x,y,z) -> str:
    return str(x)+","+str(y)+","+str(z)

def are_nodes_neighbours(node1: Node, node2: Node) -> bool:
    if abs(node1[0]-node2[0]) > 1:
        return False

    if abs(node1[1]-node2[1]) > 1:
        return False

    if abs(node1[2]-node2[2]) > 1:
        return False

    if node1[0] == node2[0] and node1[1] == node2[1] and node1[2] == node2[2]:
        return False #this is the same node

    return True

def count_active_neighbours(node: Node, allnodes: List[Node]) -> int:
    count = 0

    for n in allnodes:
        if are_nodes_neighbours(node, n) and n[3] == True:
            count+=1

    return count;

def pad_grid(allnodes: List[Node], nodenames: Set[str]) -> Tuple[List[Node], Set[str]]:
    maxz = 0
    minz = 0
    maxy = 0
    miny = 0
    maxx = 0
    minx = 0
    
    for n in allnodes:
        if n[0] > maxx:
            maxx = n[0]
        if n[0] < minx:
            minx = n[0]

        if n[1] > maxy:
            maxy = n[1]
        if n[1] < miny:
            miny = n[1]

        if n[2] > maxz:
            maxz = n[2]
        if n[2] < minz:
            minz = n[2]    

    for x in range(minx-1,maxx+2,1):
        for y in range(miny-1,maxy+2,1):
            for z in range(minz-1,maxz+2,1):
                nodename = generate_node_name(x,y,z)
                if (nodename in nodenames) == False:
                    allnodes.append((x,y,z,False))
                    nodenames.add(nodename)

    return (allnodes, nodenames)


def display_grid(nodes: List[Node]):
    maxz = 0
    minz = 0
    maxy = 0
    miny = 0
    maxx = 0
    minx = 0

    for n in nodes:
        if n[0] > maxx:
            maxx = n[0]
        if n[0] < minx:
            minx = n[0]

        if n[1] > maxy:
            maxy = n[1]
        if n[1] < miny:
            miny = n[1]

        if n[2] > maxz:
            maxz = n[2]
        if n[2] < minz:
            minz = n[2]
    
    for z in range(minz,maxz+1,1):
        print("z=",z, sep='')
        for y in range(miny,maxy+1,1):
            line = []
            for x in range(minx,maxx+1,1):
                node = [n for n in nodes if n[0] == x and n[1] == y and n[2]==z]
                if len(node) == 1:
                    if node[0][3]:
                        line.append('#')
                    else:
                        line.append('.')
                else:
                    line.append('.')
            print(''.join(line))
        print(' ')

def run_part1(filename: str, cycles: int):
    nodes = get_input(filename)
    nodenames = set( [ generate_node_name(n[0],n[1],n[2]) for n in nodes] )

    display_grid(nodes)

    cycle = 1
    while cycle <= cycles:
        pad_grid(nodes,nodenames)
        newnodes = list()
        for node in nodes:
            count = count_active_neighbours(node, nodes)
            if count == 3 and node[3] == False: #if it's inactive and has 3 active neighbours it's live
                newnodes.append( (node[0],node[1], node[2], True))
            elif (count == 3 or count == 2) and node[3] == True: # stay live if 2 or 3 active neighbour
                newnodes.append(node)
            else: #any other case the node is inactive
                newnodes.append( (node[0],node[1], node[2], False))

        #display_grid(newnodes)
        nodes = newnodes
        cycle+=1

    activenodes = [n for n in nodes if n[3]]

    print(len(activenodes))


Node2 = Tuple[int,int,int,int,bool] #,x,y,z,w,state

def get_input_day2(filename: str) ->List[Node2]:
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    nodes = list()
    for y in range(0,len(lines)):
        for x in range(0, len(lines[y])):
            if lines[y][x] == '#':
                nodes.append( (x,y,0,0,True) )
            else:
                nodes.append( (x,y,0,0,False) )

    return nodes

def generate_node_name_day2(x,y,z,w) -> str:
    return str(x)+","+str(y)+","+str(z)+","+str(w)

def are_nodes_neighbours_day2(node1: Node2, node2: Node2) -> bool:
    if abs(node1[0]-node2[0]) > 1:
        return False

    if abs(node1[1]-node2[1]) > 1:
        return False

    if abs(node1[2]-node2[2]) > 1:
        return False

    if abs(node1[3]-node2[3]) > 1:
        return False

    if node1[0] == node2[0] and node1[1] == node2[1] and node1[2] == node2[2] and node1[3] == node2[3]:
        return False #this is the same node

    return True

def count_active_neighbours_day2(node: Node2, allnodes: List[Node2]) -> int:
    count = 0

    for n in allnodes:
        if are_nodes_neighbours_day2(node, n) and n[4] == True:
            count+=1

    return count;


def pad_grid_day2(allnodes: List[Node2], nodenames: Set[str]) -> Tuple[List[Node2], Set[str]]:
    maxz = 0
    minz = 0
    maxy = 0
    miny = 0
    maxx = 0
    minx = 0
    maxw = 0
    minw = 0
    
    for n in allnodes:
        if n[0] > maxx:
            maxx = n[0]
        if n[0] < minx:
            minx = n[0]

        if n[1] > maxy:
            maxy = n[1]
        if n[1] < miny:
            miny = n[1]

        if n[2] > maxz:
            maxz = n[2]
        if n[2] < minz:
            minz = n[2]    
        
        if n[3] > maxw:
            maxw = n[3]
        if n[3] < minw:
            minw = n[3] 

    for x in range(minx-1,maxx+2,1):
        for y in range(miny-1,maxy+2,1):
            for z in range(minz-1,maxz+2,1):
                for w in range(minw-1,maxw+2,1):
                    nodename = generate_node_name_day2(x,y,z,w)
                    if (nodename in nodenames) == False:
                        allnodes.append((x,y,z,w,False))
                        nodenames.add(nodename)

    return (allnodes, nodenames)


def run_part2(filename: str, cycles: int):
    nodes = get_input_day2(filename)
    nodenames = set( [ generate_node_name_day2(n[0],n[1],n[2],n[3]) for n in nodes] )

    cycle = 1
    while cycle <= cycles:
        print(cycle)
        pad_grid_day2(nodes,nodenames)
        newnodes = list()
        for node in nodes:
            count = count_active_neighbours_day2(node, nodes)
            if count == 3 and node[4] == False: #if it's inactive and has 3 active neighbours it's live
                newnodes.append( (node[0],node[1], node[2], node[3], True))
            elif (count == 3 or count == 2) and node[4] == True: # stay live if 2 or 3 active neighbour
                newnodes.append(node)
            else: #any other case the node is inactive
                newnodes.append( (node[0],node[1], node[2], node[3], False))

        #display_grid(newnodes)
        nodes = newnodes
        cycle+=1
        

    activenodes = [n for n in nodes if n[4]]

    print(len(activenodes))



#filename = 'test.txt'
filename = 'input.txt'
cycles= 6
#run_part1(filename, cycles)

run_part2(filename, cycles)
