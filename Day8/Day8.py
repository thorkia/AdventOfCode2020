def run_instructions(instruction_set):
    accumulator = 0
    executedcommands = set()
    pointer = 0

    while pointer < len(instruction_set):
        instruction = instruction_set[pointer]  
        executedcommands.add(pointer)
        if instruction[0] == 'nop':
            pointer+=1
        elif instruction[0] == 'acc':
            accumulator+=instruction[1]
            pointer+=1
        elif instruction[0] == 'jmp':
            pointer+=instruction[1]        

        if pointer in executedcommands:
            break
     
    return (accumulator, pointer)


instructions = list();

with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    instruct = line.split(' ')
    instructions.append( (instruct[0].strip(), int(instruct[1])) )

#Part 1: Check what the accumulator is before the repeat is run
accumulator = 0
pointer = 0

accumulator,pointer = run_instructions(instructions)
print(accumulator)

index = 0
while index < len(instructions):
    #swap the instruction
    accumulator = 0
    pointer = 0
    instruction = instructions[index]

    if instruction[0] == 'nop':
        instructions[index] = ('jmp', instruction[1])
    elif instruction[0] == 'jmp':
        instructions[index] = ('nop', instruction[1])

    accumulator,pointer = run_instructions(instructions)
    if pointer == len(instructions):
        break

    #swap the instruction back if it doesn't finish
    instructions[index] = instruction    

    index+=1


print(accumulator)

#print(instructions)