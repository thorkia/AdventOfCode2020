#Set up Row and column lists
rows = [*range(128)]
columns = [*range(8)]


def get_row_number(rowcode):
    rowcode= str(rowcode)
    seatnumber = rows
    for c in rowcode:
        if c == 'F':
            seatnumber = seatnumber[: int(len(seatnumber)/2)]
        elif c =='B':
            seatnumber = seatnumber[int(-(len(seatnumber)/2)):]
    return seatnumber[0]

def get_column_number(columncode):
    columncode = str(columncode)
    seatnumber = columns
    for c in columncode:
        if c == 'L':
            seatnumber = seatnumber[: int(len(seatnumber)/2)]
        elif c =='R':
            seatnumber = seatnumber[int(-(len(seatnumber)/2)):]

    return seatnumber[0]

with open('input.txt') as f:
    lines = f.readlines()

#Part 2: Get every seat ID
seat_id_list = [ ]

#Part 1: Get highest seat ID
seatid = -1
for line in lines:
    line = line.strip()

    ticket_id = get_row_number(line[:7]) * 8 + get_column_number(line[-3:])
    seat_id_list.append(ticket_id);
    if ticket_id > seatid:
        seatid = ticket_id;

    #print(get_row_number(line[:7]), get_column_number(line[-3:]), sep=',')

print(seatid)

#Part 2: Find the missing seat ID
seat_id_list.sort()

for n in range( len(seat_id_list) - 1):
    if seat_id_list[n+1] - seat_id_list[n] == 2:
        print(seat_id_list[n], seat_id_list[n+1], sep=',')


