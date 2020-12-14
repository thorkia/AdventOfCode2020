from typing import List, Tuple, Dict
import itertools


def load_instructions(filename: str) -> List[Tuple[str,List[Tuple[int,int]]]]:
    with open(filename) as f:
        lines = f.readlines()
    mask = ''
    instructions = []

    instruction_set = []
    
    for line in lines:
        subline = [l.strip() for l in line.split('=')]
        if subline[0] == 'mask':
            if mask != '': #set the mask set
                instruction_set.append( (mask,instructions))
                mask = ''
                instructions = []
            mask = subline[1]
        else:
            val = int(subline[1])
            loc = int(subline[0][4:subline[0].index(']')])
            instructions.append( (loc,val))

    instruction_set.append( (mask,instructions)) #append the last instruction set generated
    return instruction_set

def apply_mask(mask: str, binnum:str) -> str:
    newnum = [None]*36

    for i in range(0,36,1):        
        newnum[i] = binnum[i] if mask[i]=='X' else mask[i]

    return ''.join(newnum)

def run_part1(filename: str):
    instructionset = load_instructions(filename)

    memory = dict()

    for mask,instructions in instructionset:
        for loc,inst in instructions:
            stringInst = '{0:036b}'.format(inst)
            strval = apply_mask(mask, stringInst)
            memory[loc] = int(strval,2)

    print(sum(memory.values()))

def apply_memory_mask(mask: str, memory:str) -> List[str]:
    memlocs = list()

    #get number of X:
    x_count = mask.count('X')
    allcombos = list(itertools.product([0, 1], repeat=x_count)) #generate every possible value for X

    for xcombo in allcombos:
        newnum = [None]*36
        x_index = 0
        for i in range(0,36,1):        
            if mask[i] == 'X':
                newnum[i] = str(xcombo[x_index])
                x_index+=1
            elif mask[i] == '1':
                newnum[i] = mask[i]
            else:
                newnum[i] = memory[i] #if the mask is 0, use the memory loc
        memlocs.append(''.join(newnum))
    
    return memlocs



def run_part2(filename: str):
    instructionset = load_instructions(filename)

    memory = dict()

    for mask,instructions in instructionset:
        for loc,amt in instructions:

            strmemval = '{0:036b}'.format(loc)
            #now the mask returns all possible memory values
            memvals = apply_memory_mask(mask, strmemval)
            for memval in memvals:
                memory[int(memval,2)] = amt            

    print(sum(memory.values()))




#filename='test.txt'
filename='input.txt'

run_part1(filename)

#filename='test2.txt'
run_part2(filename)

