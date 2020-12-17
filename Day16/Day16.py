
from typing import List, Tuple

Rule = Tuple[str, Tuple[int,int], Tuple[int,int]]

def get_rules(lines: List[str]) -> List[Rule]:
    rules = list()

    for line in lines:
        ticketlabel = line[:line.index(':')].strip()

        fieldslist = line[line.index(':')+1:].strip()
        firstpart = fieldslist[:fieldslist.index('or')].strip().split('-')
        secondpart = fieldslist[fieldslist.index('or')+2:].strip().split('-')

        item = (ticketlabel, (int(firstpart[0]), int(firstpart[1])), (int(secondpart[0]), int(secondpart[1])))
        rules.append(item)

    return rules

def read_file(filename: str) -> Tuple[List[Rule],List[int],List[List[int]]]:
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    
    breakline = lines.index('')
    rules = get_rules(lines[:breakline])
    yourticket = [int(n) for n in lines[lines.index('your ticket:')+1].strip().split(',') if n.isnumeric()]

    nearbytickets = list()
    for line in lines[lines.index('nearby tickets:')+1:]:
        items = [int(n) for n in line.strip().split(',') if n.isnumeric()]
        nearbytickets.append(items)

    return (rules,yourticket,nearbytickets)

def check_rule(rule: Rule, value: int) -> bool:
    return (value>=rule[1][0] and value<=rule[1][1]) or (value>=rule[2][0] and value<=rule[2][1])


def check_ticket(ticket: List[int], rules: List[Rule]) -> List[int]:
    badvalues = list()

    for ticketnumber in ticket:
        validlist = [check_rule(rule,ticketnumber) for rule in rules]
        if all(v == False for v in validlist) == True: #if the number doesn't mean any rules record it
            badvalues.append(ticketnumber)

    return badvalues


def run_part1(filename: str) -> int:
    rules, myticket, nearbytickets = read_file(filename)

    badnumbers = list()

    for ticket in nearbytickets:
        badvalues = check_ticket(ticket, rules)
        for badval in badvalues:
            badnumbers.append(badval)
            

    return sum(badnumbers)


def run_part2(filename: str) -> int:
    rules, myticket, nearbytickets = read_file(filename)

    good_tickets = [ticket for ticket in nearbytickets if len(check_ticket(ticket, rules)) == 0]

    numberoffields = len(rules)
    valid_location = dict()
          
    match_count = dict()
    match_index_list = dict()
    for rule in rules:
        index = 0
        count = 0
        matched_index = list()
        while index < numberoffields:
            validlist = [check_rule(rule, ticket[index]) for ticket in good_tickets]
            allvalid = all(v for v in validlist) #these will all be true if valid
            if allvalid == True:
                count+=1
                matched_index.append(index)

            index+=1            
        match_count[rule[0]] = count
        match_index_list[rule[0]] = matched_index

    #There should be a rule that matches only 1 column
    #find the one with one entry, then remove that index from every item in the match index list
    while len(match_index_list) > 0:
        
        #find all the matches that have 1 item - this should only return 1
        matches = [ k for k in match_index_list.keys() if len(match_index_list[k]) == 1]        

        if len(matches) > 1:
            raise Exception(matches)

        matchkey = matches[0]
        matchindex = match_index_list[matchkey][0]
        #add this the dictionary of valid fields and index
        valid_location[matchkey] = matchindex
        #remove it from the matched index list so we don't process it
        match_index_list.pop(matchkey)

        #remove the field index from every other item
        for v in match_index_list.values():
            if matchindex in v:
                v.remove(matchindex)        



    ticket_val = 1

    for k,v in valid_location.items():
        if k.startswith('departure'):
            ticket_val*=(myticket[v])

    return ticket_val



#filename='test.txt'
#filename='test2.txt'
filename='input.txt'

print(run_part1(filename))
print(run_part2(filename))