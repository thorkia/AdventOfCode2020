from typing import List

def init_board(filename:str) -> List[List[str]]:
    with open(filename) as f:
        lines = [ list(line.strip()) for line in f.readlines()]    
    
        return lines

def check_if_same(board1:List[List[str]], board2:List[List[str]]) -> bool:
    x = 0
    y = 0
    while y < len(board1):
        x = 0
        while x < len(board1[y]):
            if board1[y][x] != board2[y][x]:
                return False
            x+=1
        y+=1

    return True


#Part 1 Rules
def apply_rules_to_board(board:List[List[str]]) -> List[List[str]]:
    newBoard = []
    x = 0
    y = 0
    while y < len(board):        
        x = 0
        newRow = []
        while x < len(board[y]):
            newRow.append(new_seat_state(x,y,board))
            x+=1
        y+=1
        newBoard.append(newRow)
                
    return newBoard

def new_seat_state(x: int, y: int, board:List[List[str]]) -> str:
    if board[y][x] == '.':
        return '.'

    neighbourcount=occupied_neighbour_count(x,y, board)
    #If empty and no neighbour, sit down
    if board[y][x] == 'L' and neighbourcount == 0:
        return '#'
    #If sitting and 4 or neighbours, leave
    if board[y][x] == '#' and neighbourcount >= 4:
        return 'L'

    #Otherwise nothing changes
    return board[y][x]

def occupied_neighbour_count(x: int, y: int, board:List[List[str]]) -> int:
    count = 0;
    #Check current Row
    if x-1>=0 and board[y][x-1] == '#':
        count+=1
    if x+1<len(board[0]) and board[y][x+1] == '#':
        count+=1

    #Count row above
    if y-1>=0:
        if x-1>=0 and board[y-1][x-1] == '#':
            count+=1
        if x+1<len(board[0]) and board[y-1][x+1] == '#':
            count+=1
        if board[y-1][x] == "#":
            count+=1

    #Check row below
    if y+1<len(board):
        if x-1>=0 and board[y+1][x-1] == '#':
            count+=1
        if x+1<len(board[0]) and board[y+1][x+1] == '#':
            count+=1
        if board[y+1][x] == "#":
            count+=1


    return count


#Part 2 rules:
def apply_rules_to_board_part2(board:List[List[str]]) -> List[List[str]]:
    newBoard = []
    x = 0
    y = 0
    while y < len(board):        
        x = 0
        newRow = []
        while x < len(board[y]):
            newRow.append(new_seat_state_part2(x,y,board))
            x+=1
        y+=1
        newBoard.append(newRow)
                
    return newBoard

def new_seat_state_part2(x: int, y: int, board:List[List[str]]) -> str:
    if board[y][x] == '.':
        return '.'

    neighbourcount=occupied_neighbour_count_part2(x,y, board)
    #If empty and no neighbour, sit down
    if board[y][x] == 'L' and neighbourcount == 0:
        return '#'
    #If sitting and 4 or neighbours, leave
    if board[y][x] == '#' and neighbourcount >= 5:
        return 'L'

    #Otherwise nothing changes
    return board[y][x]

def occupied_neighbour_count_part2(x: int, y: int, board:List[List[str]]) -> int:
    count = 0;
    #Check left in current row
    newX = x-1
    while newX >= 0 and board[y][newX] != 'L':
        if board[y][newX] == '#':
            count+=1
            break
        newX-=1
    #check Right in current row
    newX = x+1
    while newX < len(board[y]) and board[y][newX] != 'L':
        if board[y][newX] == '#':
            count+=1
            break
        newX+=1

    #check up in CurrentRow
    newY = y-1
    while newY >= 0 and board[newY][x] != 'L':
        if board[newY][x] == '#':
            count+=1
            break
        newY-=1
    #check Down in current row
    newY = y+1
    while newY < len(board) and board[newY][x] != 'L':
        if board[newY][x] == '#':
            count+=1
            break
        newY+=1

    #Check up and left
    newY = y-1
    newX = x-1
    while newY >= 0 and newX >= 0 and board[newY][newX] != 'L':
        if board[newY][newX] == '#':
            count+=1
            break
        newY-=1
        newX-=1

    #Check down and right
    newY = y+1
    newX = x+1
    while newY < len(board) and newX < len(board[newY]) and board[newY][newX] != 'L':
        if board[newY][newX] == '#':
            count+=1
            break
        newY+=1
        newX+=1


    #Check up and right
    newY = y-1
    newX = x+1
    while newY >= 0 and newX < len(board[newY]) and board[newY][newX] != 'L':
        if board[newY][newX] == '#':
            count+=1
            break
        newY-=1
        newX+=1

    #Check down and left
    newY = y+1
    newX = x-1
    while newY < len(board) and newX >= 0 and board[newY][newX] != 'L':
        if board[newY][newX] == '#':
            count+=1
            break
        newY+=1
        newX-=1
  


    return count

def display_board(board:List[List[str]]):
    for row in board:
        print("".join(row))
    print(' ')

startboard = init_board('input.txt')

previousboard = startboard
roundcount = 0

while True:
    
    newboard = apply_rules_to_board(previousboard)

    if check_if_same(previousboard,newboard):
        break

    roundcount +=1
    previousboard = newboard;


print(roundcount)
count = sum( n.count('#') for n in previousboard )
print(count)


print('Part2')
#Part 2
part2prev = startboard
roundcount = 0
while True:
    
    newboard = apply_rules_to_board_part2(part2prev)
    #display_board(newboard)

    if check_if_same(part2prev,newboard):
        break

    roundcount +=1
    part2prev = newboard;


print(roundcount)
count = sum( n.count('#') for n in part2prev )
print(count)



